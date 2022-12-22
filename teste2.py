from classes.ChainingHashTable import ChainingHashTable
import socket
from threading import Semaphore

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
'''
a = 10
b = 10.5

print(type(a))
print(type(b))

if type(a) == int or float:
    print('a entrou')

if type(b) == int or float:
    print('b entrou')

while True:
    while True:
        break

    print('paciencia')
    break
'''


a = Semaphore() # 1

a.acquire() # 0
a.release() # 1
a.release() # 1 ou 2

a.acquire() # 0 ou 1
a.acquire() # -1 ou 0

