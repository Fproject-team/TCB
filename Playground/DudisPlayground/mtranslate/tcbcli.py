import click

def banner():
    click.echo("""
    \033[95m _____ _      _        _      ____ _               _  __       _               ____   ___ _____  \033[0m
    \033[95m|_   _(_) ___| | _____| |_   / ___| | __ _ ___ ___(_)/ _|_   _(_)_ __   __ _  | __ ) / _ \_   _| \033[0m
    \033[95m  | | | |/ __| |/ / _ \ __| | |   | |/ _` / __/ __| | |_| | | | | '_ \ / _` | |  _ \| | | || |   \033[0m
    \033[95m  | | | | (__|   <  __/ |_  | |___| | (_| \__ \__ \ |  _| |_| | | | | | (_| | | |_) | |_| || |   \033[0m
    \033[95m  |_| |_|\___|_|\_\___|\__|  \____|_|\__,_|___/___/_|_|  \__, |_|_| |_|\__, | |____/ \___/ |_|   \033[0m
    \033[95m                                                         |___/         |___/                     \033[0m """)

@click.group()
def server():
    pass

@server.command(help = "Start TCB Server")
def start():
    from subprocess import call
    click.echo('Starting TCB server') 
    call(["python", "receive.py"])
    click.echo('TCB server is started')

@server.command(help = "Stop TCB Server")
def stop():
     click.echo('Stoping TCB server')
     # PLACEHOLDER - Command for starting TCB Server
     click.echo('TCB server is stoped')

@server.command(help = "Train TCB")
def train():
     click.echo('Starting to train ')

@server.command(help = "Upload new training set to TCB")
def upload():
     click.echo('Starting Upplad')


server.add_command(start)
server.add_command(stop)
server.add_command(train)
server.add_command(upload)

if __name__ == '__main__':

    banner()
    server()