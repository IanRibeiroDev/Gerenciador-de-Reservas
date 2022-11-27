from listaEncadeada import listaEncadeada

class Reserva:
    def __init__(self):
        self.__meses = listaEncadeada()

        for i in range(1,13):
            nomeVariavel = 'mes' + str(i)
            temp = vars()[nomeVariavel] = listaEncadeada()
            temp.insereFim('Deu certo' + str(i))
            self.__meses.insereFim(temp)
        
        
    def getter(self):
        for i in range(1,13):
            print(self.__meses.elemento(i))

'''
for i in range(1,10):
    resultado = 'lol' + str(i)
    variavel = 'ano' + str(i)
    vars()[variavel] = resultado

print(ano5)

lista = [[1[50,51,52],2[60,61,62],3,4],10,11]
'''
'''
lp = listaEncadeada()
nomeVariavel = 'mes' + '1'
temp = vars()[nomeVariavel] = listaEncadeada('Funciona')

nomeVariavel = 'mes' + '2'
temp2 = vars()[nomeVariavel] = listaEncadeada('Bem!')
lp.insereInicio(temp)
lp.insereFim(temp2)
print(lp)

lista2 = ['isso']
lista3 = ['aquilo']
lista1 = [lista2, lista3]

print(lista1)
'''

a = Reserva()
a.getter()