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