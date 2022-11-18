from socket import *

host=gethostname()
port = 55551

print(f'HOST: {host},PORT:{port}')

cli = socket(AF_INET,SOCK_STREAM)
cli.connect((host,port))


while True:
    msg = input("Digite: ")
    cli.send(msg.encode())