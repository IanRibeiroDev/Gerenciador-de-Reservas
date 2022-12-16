import socket
#import threading
#from b import * 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def startBinding(port):
    server_address = ('localhost', port)
    return server_address

if __name__ == "__main__":
    server_address = startBinding(20000)
    message = ''
    print('Bem-vind@. Digite Menu para começar')

    while message != '5':

        message = input('Digite a mensagem: ')

        sock.sendto(message.encode(), server_address)
        #client_thread = threading.Thread(target=sendMessage, args=(data, address))

        data, address = sock.recvfrom(1024)
        print(f'Servidor: {data.decode()}')
        data = '' 
