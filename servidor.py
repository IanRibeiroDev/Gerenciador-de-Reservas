import socket
import threading
from classes.GerenciadorClientes import GerenciadorClientes

gerenciador = GerenciadorClientes()

host = 'localhost'
porta = 60000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, porta))

print(f'Servidor {host} online na porta {porta}')


def handleClient(client_msg, client_address):

    msg = client_msg.decode().split('-')
    print(f'Cliente {client_address}: {msg}')

    response = gerenciador.handleMsg(msg)
    sock.sendto(response.encode(), client_address)
    print(f'Servidor: {response}')


while True:
    client_msg, client_address = sock.recvfrom(4096)

    # Troca de mensagens acontece através de threads:
    #client_thread = threading.Thread(target=handleClient, args=(client_msg, client_address))
    #client_thread.start()
    handleClient(client_msg, client_address)