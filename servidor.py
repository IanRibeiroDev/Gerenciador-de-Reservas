import socket
import threading
from protocolo import validateMessage

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def startServer(port):
    server_address = ('localhost', port)
    sock.bind(server_address)
    return print(f"Servidor iniciado em {server_address[0]} porta {server_address[1]}")

def sendMessage(data, address):
    print("Enviando mensagem: {0} to address: {1}".format(data, address))
    sock.sendto(data.encode(), address)


startServer(20000)
while True:
    data, address = sock.recvfrom(1024)
    sendMessage(validateMessage(data), address)

    data = '' 
    address = ''

        #client_thread = threading.Thread(target=receive, args=(data, address))
        #client_thread = threading.Thread(target=validateMessage, args=(data)
        #validadeMessage(data)

        #client_thread.start()
        