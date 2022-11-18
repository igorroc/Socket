from socket import *
import utils.terminal as cmd

HOST = gethostname()
PORT = 55551


cmd.clear_screen()
print('Tentando se conectar ao servidor...')
print(f'HOST: {HOST},PORT:{PORT}')
cmd.delay_loading(5)
cmd.clear_screen()

server = socket(AF_INET, SOCK_STREAM)
server.connect((HOST, PORT))

msg = server.recv(1024)
print(msg.decode())

while True:
    msg = input("Digite: ")
    server.send(msg.encode())
