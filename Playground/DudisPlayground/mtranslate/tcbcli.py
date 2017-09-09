import click
import os
import sys

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
    click.echo('Starting TCB server') 
    os.system("python receive.py &")
    click.echo('TCB server is started')

@server.command(help = "Stop TCB Server")
def stop():
     click.echo('Stoping TCB server')
     os.system("pkill -f receive.py")
     click.echo('TCB server is stoped')

@server.command(help = "Train TCB")
def train():
    from Classify.classifyTrainDbOrganize import classify
    click.echo('Starting to train')
    classify()

@server.command(help = "Upload new training set to TCB")
@click.option('--path', help='The pass to the CSV file')
@click.option('--orgname',help='The name of the organization')
def upload(path,prgname):
    import Files.ReadFromCSVTry
    click.echo('Starting Upplad')
    ReadFromCSV(path,orgname)



server.add_command(start)
server.add_command(stop)
server.add_command(train)
server.add_command(upload)

if __name__ == '__main__':

    banner()
    server()