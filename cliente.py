from socket import *
import utils.terminal as cmd

HOST = gethostname()
PORT = 55551
BUFFER = 1024


cmd.clear_screen()
print('Tentando se conectar ao servidor...')
print(f'HOST: {HOST},PORT:{PORT}')
cmd.delay_loading(10)
cmd.clear_screen()

server = socket(AF_INET, SOCK_STREAM)
server.connect((HOST, PORT))


while True:
    msg = server.recv(BUFFER)

    if msg.decode() == 'close':
        print('Conexão encerrada com o servidor')
        server.close()
        break

    print(msg.decode())

    frase = input("Digite: ")
    server.send(frase.encode())
