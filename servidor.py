from socket import *
import utils.inteligencia as ia
import utils.terminal as cmd

HOST = gethostname()
PORT = 55551
MAX_QUEUE = 5

cmd.clear_screen()
cmd.server_loading()
cmd.clear_screen()

print(f'Servidor iniciado no host: {HOST}')
print(f'Utilizando a porta: {PORT}')
print('Aguardando conexões...')

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(MAX_QUEUE)

while True:
    clientSocket, address = server.accept()
    print(f'Conexão estabelecida com o cliente: {address}')
    clientSocket.send('Conexão estabelecida com o servidor'.encode())
    while True:
        msg = clientSocket.recv(1024)
        msg = msg.decode()

        if msg == 'sair':
            print(colorama.Fore.LIGHTRED_EX + f'- Conexão encerrada com o cliente: {address}')
            clientSocket.send('close'.encode())
            # clientSocket.close()
            break

        fraseInterpretada = ia.interpreta_frase(msg)
        clientSocket.send(fraseInterpretada.encode())
