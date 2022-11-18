from socket import *
import utils.terminal as cmd
import colorama

HOST = gethostname()
PORT = 55551
BUFFER_SIZE = 1024


def main():
    cmd.clear_screen()
    print('Tentando se conectar ao servidor...')
    print(f'HOST: {HOST},PORT:{PORT}')
    cmd.delay_loading(10)
    cmd.clear_screen()

    try:
        server = socket(AF_INET, SOCK_STREAM)
        server.connect((HOST, PORT))
    except:
        print(colorama.Fore.LIGHTRED_EX +
              '\n- Não foi possível se conectar ao servidor. Ele está ativo?')
        return cmd.clear_terminal_color()

    # Instruções para o cliente
    msg = server.recv(BUFFER_SIZE)
    while msg.decode() != 'start':
        print(msg.decode())
        msg = server.recv(BUFFER_SIZE)

    # Captura o nome do usuário
    print("\n")
    print("Digite seu nome de usuário:")
    nome = input("> ")
    server.send(nome.encode())

    print('\n')
    print("No que você está pensando?")
    # Loop de interação com o servidor
    while msg.decode() != 'close':
        frase = input("> ")
        server.send(frase.encode())

        msg = server.recv(BUFFER_SIZE)
        if msg.decode() != 'close':
            print(msg.decode())
            print('\n')

    print('\n')
    print(colorama.Fore.LIGHTRED_EX + f'- Conexão encerrada com o servidor')
    server.close()
    cmd.clear_terminal_color()


main()
