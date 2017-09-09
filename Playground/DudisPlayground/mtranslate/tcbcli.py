#!/usr/bin/env python
from tfmodule import TFModule
from tfutils import decrypted, cd
from os import path
from playbook import Playbook
import hashlib
import os
import sys
import validator
import updates
import logger
import state
import error
from executor import terraform_executor

try:
    import click
except ImportError:
    print('Please pip install "click>=6.0"')
    sys.exit(1)

TERRAFLOW_DIR = path.abspath(path.dirname(__file__))


def banner():
    header = """\033[95m _____                    __ _                \033[0m
\033[95m|_   _|__ _ __ _ __ __ _ / _| | _____      __ \033[0m
\033[95m  | |/ _ \ '__| '__/ _` | |_| |/ _ \ \ /\ / / \033[0m
\033[95m  | |  __/ |  | | | (_| |  _| | (_) \ V  V /  \033[0m
\033[95m  |_|\___|_|  |_|  \__,_|_| |_|\___/ \_/\_/   \033[0m
    """

    print header


def get_playbooks_hash():
    """
        Compute MD5 hash for all our playbooks.
        We use this to detect changes between plan and apply
        By following symlinks we also guarantee we walk through the modules and not just states.

    :return: MD5 of all the state folders in the playbooks
    """

    hash_md5 = hashlib.md5()
    for playbook in state.playbooks:
        for step in playbook.steps:
            with cd(step.state_dir):
                with decrypted():
                    for subdir, dirs, files in os.walk('.', followlinks=True):
                        for file in files:
                            full_path = os.path.join(subdir, file)
                            with open(full_path, "rb") as f:
                                for chunk in iter(lambda: f.read(4096), b""):
                                    hash_md5.update(chunk)

    return hash_md5.hexdigest()

def load_playbooks(playbooks, tag=None):
    """
        Load playbooks into state
    :param playbooks:
    :return:
    """
    for playbook_file in playbooks:
        p = Playbook(book_file=playbook_file, tag=tag)
        state.playbooks.append(p)


def get_multilock_names():
    """
        We need to lock all the states before we begin our run
        This to prevent our run failing in the middle due to locks
    :return: array of lock names, with all the state names from all of our playbooks
    """

    locks = set()

    for playbook in state.playbooks:
        for step in playbook.steps:
            module_name, state_name = state.get_module_and_state_name(step.state_dir)
            lock_name = '{}_{}'.format(module_name, state_name)
            locks.add(lock_name)

    return list(locks)


def validate_playbooks():
    """
        Validate all playbooks
    :return:
    """

    for playbook in state.playbooks:
        logger.colored_log('* Validating playbook "{}"...'.format(playbook.book_file), fg='yellow')
        playbook.validate()


def runner(cmd):
    """
        Run a terraform command on all the playbooks by order
    :param cmd:
    :return:
    """

    try:
        for playbook in state.playbooks:
            state.active_playbook = playbook
            playbook.terraform(cmd)
    except error.TerraformCommandException, ex:
        logger.colored_log('Execution of {} ({}) failed'.format(
            state.active_playbook,
            state.active_step), fg='red')


@click.group()
@click.option('--quiet/--no-quiet', default=False)
def cli(quiet):
    banner()


@cli.command('plan')
@click.argument('playbooks', nargs=-1, type=click.Path(exists=True))
@click.option('--tag', default=[], multiple=True)
def plan(playbooks, tag):
    load_playbooks(playbooks, tag)
    validate_playbooks()
    runner('get')
    runner('plan')


@cli.command('decrypt')
@click.argument('playbooks', nargs=-1, type=click.Path(exists=True))
@click.option('--tag', default=[], multiple=True)
def decrypt(playbooks, tag):
    """
    Will decrypt the .tfstate.encrypted and .tfstate.backup.encrypted
    files for all the states in the provided playbook
    """
    load_playbooks(playbooks, tag)
    runner('decrypt')


@cli.command('encrypt')
@click.argument('playbooks', nargs=-1, type=click.Path(exists=True))
@click.option('--tag', default=[], multiple=True)
def encrypt(playbooks, tag):
    """
    Will encrypt (and remove) the .tfstate files
    for all the states in the provided playbook
    """
    load_playbooks(playbooks, tag)
    validate_playbooks()
    runner('encrypt')


@cli.command('get')
@click.argument('playbooks', nargs=-1, type=click.Path(exists=True))
def get(playbooks):
    load_playbooks(playbooks, tag)
    validate_playbooks()
    runner('get')


@cli.command('destroy')
@click.argument('playbooks', nargs=-1, type=click.Path(exists=True))
@click.option('--tag', default=[], multiple=True)
def destroy(playbooks, tag):
    load_playbooks(playbooks, tag)
    validate_playbooks()

    runner('get')

    playbooks_hash = get_playbooks_hash()

    runner('plan -destroy -module-depth=-1')

    confirm = raw_input("Are you sure you'd like to destroy ({})? [yes|no]: ".format(playbooks_hash))
    if confirm == 'yes':
        runner('destroy')


@cli.command('apply')
@click.argument('playbooks', nargs=-1, type=click.Path(exists=True))
@click.option('--tag', default=[], multiple=True)
def apply(playbooks, tag):
    load_playbooks(playbooks, tag)
    validate_playbooks()

    runner('get')

    playbooks_hash = get_playbooks_hash()

    runner('plan')

    confirm = raw_input("Are you sure you'd like to apply ({})? [yes|no]: ".format(playbooks_hash))
    if confirm == 'yes':
        new_hash = get_playbooks_hash()
        if new_hash != playbooks_hash:
            logger.colored_log("Module has changed! Aborting apply. Please run again.",
                                fg='red', bold=True)
            return

        runner('apply')


@cli.command('init')
@click.argument('module_name')
def init(module_name):
    tf = TFModule(module_name=module_name)
    tf.create()


if __name__ == '__main__':
    if updates.should_update():
        logger.colored_log('Warning: ', fg='yellow')
        click.echo("You're not running the latest version of terraflow\n"
                   "Upgrade instructions:\n"
                   "  cd {}\n"
                   "  git pull -r\n".format(TERRAFLOW_DIR)
                   )

    validator.validate_terraform_version()
    cli()
