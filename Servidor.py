import socket
import threading

HOST = 'localhost'
PORT = 5000

def handle_client(conn, addr):
    print(f'Conectado por {addr}')
    while True:
        # Recebe o número enviado pelo produtor
        data = conn.recv(1024)
        num = int(data.decode())
        if num == 0:
            # Termina a conexão quando recebe o número zero
            conn.close()
            break
        # Verifica se o número é primo
        primo = True
        if num == 1:
            primo = False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primo = False
                break
        # Envia a resposta ao produtor
        if primo:
            conn.send(b'1')
        else:
            conn.send(b'0')

# Cria o socket do servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liga o socket à porta e endereço definidos
sock.bind((HOST, PORT))
print("Aguardando conexões...")

# Escuta por conexões
sock.listen()

while True:
    # Aguarda por uma conexão
    conn, addr = sock.accept()

    # Inicia uma nova thread para atender ao cliente
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
