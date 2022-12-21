import socket
import threading
from classes.GerenciadorClientes import GerenciadorClientes
from classes.ChainingHashTable import ChainingHashTable

gerenciador = GerenciadorClientes()
operacoes = ChainingHashTable(4)

operacoes.put('NEW', 'efetuar nova reserva')
operacoes.put('DEL', 'deletar reserva efetuada')
operacoes.put('LIST', 'lista de reservas efetuadas')
operacoes.put('ALT', 'alterar reserva efetuada')

'''
O que a Hash Table operacoes esta representando:

operacoes = {
    'NEW':'efetuar nova reserva',
    'DEL':'deletar reserva efetuada',
    'LIST':'lista de reservas efetuadas',
    'ALT':'alterar reserva  efetuada'
}
'''

host = 'localhost'
porta = 60000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, porta))

print(f'Servidor {host} online na porta {porta}')


def handleClient(client_msg, client_address):

    msg = client_msg.decode().split('-')

    if msg[2] == '<1>':
        print(f'Cliente {msg[3]} requisitou: {operacoes.get(msg[1])}.\n')

    resposta = gerenciador.handleMsg(msg)
    sock.sendto(resposta.encode(), client_address)


while True:
    client_msg, client_address = sock.recvfrom(4096)

    # Troca de mensagens acontece através de threads:
    #client_thread = threading.Thread(target=handleClient, args=(client_msg, client_address))
    #client_thread.start()
    handleClient(client_msg, client_address)