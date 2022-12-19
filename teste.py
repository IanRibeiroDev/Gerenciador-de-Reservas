from io import StringIO
import sys
from teste2 import funcaoPrint
from classes.ArvoreAVL import AVLTree

def publico():
    __privado('Veio do publico.')

def __privado(msg = 'Veio do privado'):
    print(msg)


class teste():
    def __init__(self) -> None:
        self.linguiça = 'delicia'
    
    def addSelf(self):
        self.teste = 'funciona'

try:
    t = teste()
    print(t.teste)
except:
    t.addSelf()
    print(t.teste)

def tes(obr, opc = 2):
    print(obr)
    print(opc)

tes(1)

'''
buffer = StringIO()
sys.stdout = buffer

print('q')
#funcaoPrint()
print_output = buffer.getvalue()

sys.stdout = sys.__stdout__

print(len('voltou ao normal'))
print(print_output)
'''

# Fazer o algoritmo reconhecer o espaço em branco como separador e ele mesmo saber que isso denomina o fim do numero

string = '1 2 3 6 9 14 17 24 31 '
arvore = AVLTree()

ponteiro = 0

while ponteiro < len(string):
    # Caso seja um número de dois dígitos.
    if string[ponteiro + 1] != ' ':
        arvore.insert(int(string[ponteiro] + string[ponteiro + 1]))
        ponteiro += 3

    # Caso seja um número de um dígito.
    else:
        arvore.insert(int(string[ponteiro]))
        ponteiro += 2


print(string)
arvore.emOrdem()

'''
Versao OG do algoritmo, caso seja necessária.

while ponteiro < len(string):
    # Caso seja um número de dois dígitos.
    if string[ponteiro] != ' ' and string[ponteiro + 1] != ' ':
        arvore.insert(int(string[ponteiro] + string[ponteiro + 1]))
        ponteiro += 1

    # Caso seja um número de um dígito.
    elif string[ponteiro] != ' ':
        arvore.insert(int(string[ponteiro]))
        ponteiro += 1

    # Caso seja um espaço vazio.
    else:
        ponteiro += 1

'''