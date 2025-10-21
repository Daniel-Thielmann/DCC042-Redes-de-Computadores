import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

# Cria o socket UDP
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Faz o bind entre endereço e porta
UDPServerSocket.bind((localIP, localPort))

print("Servidor UDP iniciado e escutando...")

while True:
    # Recebe dados do cliente
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0].decode().strip()  # decodifica bytes -> string
    address = bytesAddressPair[1]

    print(f"Mensagem do Cliente: {message}")
    print(f"Endereço IP do Cliente: {address}")

    try:
        # Espera mensagem no formato: "n1,n2,op"
        n1_str, n2_str, op = message.split(',')
        n1 = float(n1_str)
        n2 = float(n2_str)

        # Realiza o cálculo de acordo com o operador
        if op == '+':
            result = n1 + n2
        elif op == '-':
            result = n1 - n2
        elif op == '*':
            result = n1 * n2
        elif op == '/':
            if n2 == 0:
                result = "Erro: divisão por zero"
            else:
                result = n1 / n2
        else:
            result = f"Operador inválido: {op}"

    except ValueError:
        result = "Erro: formato inválido. Use n1,n2,op"
    except Exception as e:
        result = f"Erro: {str(e)}"

    # Envia a resposta de volta ao cliente
    resposta = str(result).encode()
    UDPServerSocket.sendto(resposta, address)
    print(f"Resultado enviado ao cliente: {result}\n")

