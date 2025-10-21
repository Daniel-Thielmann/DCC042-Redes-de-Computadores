import socket
import threading

HOST = "127.0.0.1"
PORTA = 34214


def ouvir_servidor(sock):
    while True:
        try:
            dados = sock.recv(1024)
            if not dados:
                print("\n[!] Servidor encerrou a conexão.")
                break
            print("\nServidor:", dados.decode())
        except:
            print("\n[!] Erro ao receber dados.")
            break


def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect((HOST, PORTA))
        print(f"[+] Conectado ao servidor {HOST}:{PORTA}\n")
    except:
        print("[!] Não foi possível conectar ao servidor.")
        return

    thread_ouvir = threading.Thread(target=ouvir_servidor, args=(cliente,))
    thread_ouvir.start()

    while True:
        msg = input("Você: ")
        if msg.lower() in ["sair", "exit"]:
            print("Encerrando chat...")
            cliente.close()
            break
        cliente.send(msg.encode())


if __name__ == "__main__":
    iniciar_cliente()
