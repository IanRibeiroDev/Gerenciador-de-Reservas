from ListaSequencial import ListaSequencial
from ListaEncadeada import ListaEncadeada
from ChainingHashTable import ChainingHashTable

class Reserva:
    def __init__(self):
        self.__meses = ListaSequencial()

        for i in range(12):
            # Verifica se o mês tem 31 dias.
            if i in [0, 2, 4, 6, 7, 9, 11]:
                dias = ChainingHashTable(31)
                self.__meses.inserir(i, dias)

            # Verifica se o mês é Fevereiro.
            elif i == 1:
                dias = ChainingHashTable(28)
                self.__meses.inserir(i, dias)

            # Se não entrou nos outros laços, então o mês tem 30 dias.
            else:
                dias = ChainingHashTable(30)
                self.__meses.inserir(i, dias)
        
    def getter(self):
        print(self.__meses)



a = Reserva()
a.getter()
