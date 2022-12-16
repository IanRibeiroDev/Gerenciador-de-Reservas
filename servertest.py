import socket
import threading
from protocolo import validateMessage


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = 'localhost'
porta = 20000
socket.bind((host, porta))
server = ('localhost', 20000)

print(f'Servidor ativo na porta {server[1]}')


def handleClient(client_data, client_address):

    data = client_data.decode()
    print(f'Cliente {client_address}: {data}')

    response = validateMessage(client_data)
    socket.sendto(response.encode(), client_address)
    print(f'Servidor: {response}')


while True:
    client_data, client_address = socket.recvfrom(4096)

    # Troca de mensagens acontece através de threads:
    client_thread = threading.Thread(target=handleClient, args=(client_data, client_address))
    client_thread.start()