from socket import *
import utils.terminal as cmd
import colorama

HOST = gethostname()
PORT = 55551
BUFFER_SIZE = 1024


def main():
    cmd.clear_screen()
    HOST = input("Digite o host que deseja conectar: ")
    PORT = int(input("Digite a porta que deseja conectar: "))
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
    USER = input(colorama.Fore.LIGHTCYAN_EX +
                 " ▶ " + colorama.Fore.RESET)
    server.send(f'name:{USER}'.encode())

    print('\n')
    print(f"No que você está pensando, {USER}?")
    # Loop de interação com o servidor
    while msg.decode() != 'close':
        frase = input(colorama.Fore.LIGHTCYAN_EX +
                      " ▶ " + colorama.Fore.RESET)
        server.send(f'{USER}:{frase}'.encode())

        msg = server.recv(BUFFER_SIZE)
        if msg.decode() != 'close':
            print('{:>40}'.format(msg.decode()) +
                  colorama.Fore.LIGHTMAGENTA_EX + ' ◀' + colorama.Fore.RESET)

    print('\n')
    print(colorama.Fore.LIGHTRED_EX + f'- Conexão encerrada com o servidor')
    server.close()
    cmd.clear_terminal_color()


main()
