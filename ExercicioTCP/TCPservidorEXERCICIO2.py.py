import socket
import threading

HOST = "127.0.0.1"
PORTA = 34214


def receber_mensagens(conexao):
    while True:
        try:
            dados = conexao.recv(1024)
            if not dados:
                print("\n[!] Cliente desconectado.")
                break
            print("\nCliente:", dados.decode())
        except:
            print("\n[!] Erro ao receber mensagem.")
            break


def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORTA))
    servidor.listen(1)

    print(f"Servidor iniciado em {HOST}:{PORTA}")
    print("Aguardando conexão do cliente...\n")

    conexao, endereco = servidor.accept()
    print(f"[+] Cliente conectado em {endereco}\n")

    thread_receber = threading.Thread(target=receber_mensagens, args=(conexao,))
    thread_receber.start()

    while True:
        msg = input("Você: ")
        if msg.lower() in ["sair", "exit"]:
            print("Encerrando chat...")
            conexao.close()
            servidor.close()
            break
        conexao.send(msg.encode())


if __name__ == "__main__":
    iniciar_servidor()
