from socket import *
import utils.inteligencia as ia
import utils.terminal as cmd
import colorama
import time

HOST = gethostname()
PORT = 55551
MAX_QUEUE = 5
BUFFER_SIZE = 1024

cmd.clear_terminal_color()
cmd.clear_screen()
cmd.server_loading()
cmd.clear_screen()

print(f'Servidor iniciado no host: {HOST}')
print(f'Utilizando a porta: {PORT}')
print('Aguardando conexões...')

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(MAX_QUEUE)

currentClients = 0


def new_client_instructions(clientSocket):
    clientSocket.send(bytes(colorama.Fore.LIGHTGREEN_EX +
                      '+ Conexão estabelecida com o servidor', 'utf-8'))
    time.sleep(0.1)
    clientSocket.send(bytes(colorama.Fore.RESET, 'utf-8'))
    clientSocket.send('Bem vindo(a) ao Analisador de Emoções!'.encode())
    time.sleep(0.1)
    clientSocket.send(
        'Para utilizar, basta digitar uma frase, e o servidor te responderá com o sentimento referente.'.encode())
    time.sleep(0.1)
    clientSocket.send(
        'Caso você deseje encerrar a conexão, basta digitar "sair"'.encode())
    time.sleep(0.2)

    clientSocket.send('start'.encode())


while True:
    clientSocket, address = server.accept()
    print(colorama.Fore.LIGHTGREEN_EX +
          f'+ Conexão estabelecida com o cliente: {address}')
    cmd.clear_terminal_color()
    new_client_instructions(clientSocket)
    while True:
        msg = clientSocket.recv(BUFFER_SIZE)
        msg = msg.decode()

        if msg == 'sair':
            print(colorama.Fore.LIGHTRED_EX +
                  f'- Conexão encerrada com o cliente: {address}')
            cmd.clear_terminal_color()
            clientSocket.send('close'.encode())
            clientSocket.close()
            break

        fraseInterpretada = ia.interpreta_frase(msg)
        clientSocket.send(fraseInterpretada.encode())
