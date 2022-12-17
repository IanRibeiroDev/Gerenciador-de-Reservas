from ListaSequencial import ListaSequencial
from ListaEncadeada import ListaEncadeada
from ArvoreAVL import AVLTree
from ChainingHashTable import ChainingHashTable

class Reservas:
    def __init__(self):
        self.__meses = ListaSequencial()

        # Cria uma AVL de dias para cada mês.
        for i in range(1, 13):
            dias = AVLTree()
            self.__meses.inserir(i, dias)


    def verificaMesasDisponíveis(self, mes, dia):
        arvoreDias = self.__meses.elemento(mes)
        hashTableReservas = arvoreDias.getHashNode(dia)
        
        if hashTableReservas == None:
            arvoreDias.insertHashNode(dia)
            hashTableReservas = arvoreDias.getHashNode(dia)

        # ---To be continued---> *Musica de encerramento de Jojo*


    def getter(self):
        print(self.__meses.elemento(1))



a = Reservas()
a.verificaMesasDisponíveis(2, 1)
