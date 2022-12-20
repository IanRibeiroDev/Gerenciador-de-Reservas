import socket

'''
def funcaoPrint():
    print('1 ')
    print('4 ')
    print('10 ')

def opcParametro(obg, opc = None):
    return

#opcParametro()

a = [1,2,3,4,5]

if a[2]:
    print('entra')

if a[10]:
    print('eita')
'''
msg = ['LIST']


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 60000)

for i in range(len(msg)):
    comando = f'CLI-{msg[i]}-<1>-Ian-2023-2-1'

    sock.sendto(comando.encode(), server_address)

    resposta, address = sock.recvfrom(1024)
        
    print(resposta.decode())