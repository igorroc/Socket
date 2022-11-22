import utils.inteligencia as ia
import colorama
import time

BUFFER_SIZE = 1024


def new_client_instructions(clientSocket):
    clientSocket.send(
        bytes(
            colorama.Fore.LIGHTGREEN_EX +
            '+ Conexão estabelecida com o servidor', 'utf-8'
        )
    )
    time.sleep(0.2)
    clientSocket.send(
        bytes(colorama.Fore.RESET, 'utf-8')
    )
    clientSocket.send(
        'Bem vindo(a) ao Analisador de Emoções!'.encode()
    )
    time.sleep(0.2)
    clientSocket.send(
        'Para utilizar, basta digitar uma frase, e o servidor te responderá com o sentimento referente.'.encode()
    )
    time.sleep(0.2)
    clientSocket.send(
        'Caso você deseje encerrar a conexão, basta digitar \'sair\''.encode()
    )
    time.sleep(0.4)

    clientSocket.send(
        'start'.encode()
    )


def handle_messages(connection, address):
    while True:
        msg = connection.recv(BUFFER_SIZE)
        msg = msg.decode().split(':')
        user = msg[0]
        msg = msg[1]

        if msg == 'sair':
            print(
                colorama.Fore.LIGHTRED_EX
                + '[LEFT_USER]: ' + colorama.Fore.RESET
                + f'{user} ' + colorama.Style.DIM
                + f'{address}' + colorama.Style.RESET_ALL
            )
            connection.send('close'.encode())
            connection.close()

            break

        fraseInterpretada = ia.interpreta_frase(msg)
        connection.send(fraseInterpretada.encode())
        print(
            colorama.Fore.LIGHTMAGENTA_EX
            + '[REQUEST]: ' + colorama.Fore.RESET +
            colorama.Fore.LIGHTCYAN_EX
            + f'@{user} ' + colorama.Fore.RESET + colorama.Style.DIM
            + f'\'{msg}\' ' + colorama.Style.RESET_ALL
            + colorama.Back.MAGENTA + f' {fraseInterpretada} '
            + colorama.Back.RESET
        )

    connection.close()
