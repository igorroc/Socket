from socket import *
import threading
import utils.terminal as cmd
import colorama
import utils.threads as ServerThreads

HOST = gethostname()
PORT = 55551
MAX_QUEUE = 5
BUFFER_SIZE = 1024

cmd.clear_terminal_color()
cmd.clear_screen()

PORT = int(input("Digite a porta que deseja utilizar: "))

cmd.server_loading()
cmd.clear_screen()

print(
    '↪ Servidor iniciado no host: ' +
    colorama.Back.LIGHTCYAN_EX + colorama.Fore.BLACK + f' {HOST} ' + colorama.Back.RESET + colorama.Fore.RESET
)
print(
    '↪ Utilizando a porta: ' +
    colorama.Back.LIGHTMAGENTA_EX + colorama.Fore.BLACK + f' {PORT} ' + colorama.Back.RESET + colorama.Fore.RESET
)

print('↪ Aguardando conexões...')

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(MAX_QUEUE)

currentClients = []

while True:
    clientSocket, address = server.accept()
    print(
        colorama.Fore.LIGHTGREEN_EX +
        f'+ Conexão estabelecida com o cliente: {address}'
        + colorama.Fore.RESET
    )

    ServerThreads.new_client_instructions(clientSocket)

    msg = clientSocket.recv(BUFFER_SIZE)
    msg = msg.decode().split('name:')[1]
    print(
        colorama.Fore.LIGHTCYAN_EX +
        '[NEW_USER]: '
        + colorama.Fore.RESET
        + msg
    )

    currentClients.append(
        {"socket": clientSocket, "address": address, "username": msg})

    thread = threading.Thread(
        target=ServerThreads.handle_messages, args=[clientSocket, address])
    thread.start()
