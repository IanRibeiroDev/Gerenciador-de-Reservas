from classes.ListaSequencial import ListaSequencial
from classes.ListaEncadeada import ListaEncadeada
from classes.GerenciadorReservas import GerenciadorReservas
import datetime

class GerenciadorClientes:
    def __init__(self) -> None:
        self.__anos = ListaSequencial()
        self.__anosPassados = ListaEncadeada()
        self.__inserirAnos()
        

    def __inserirAnos(self):
        dataAtual = datetime.date.today()
        contador = 0

        while contador < 3:
            ano = GerenciadorReservas(dataAtual.year + contador)
            self.__anos.inserir(contador + 1, ano)
            contador += 1


    def handleMsg(self, msg):
        if msg[1] == 'NEW':
            msg[4] = int(msg[4])            
            msg[5] = int(msg[5])            
            resposta = self.__anos.elemento(2).verificarMesasDisponiveis(msg[4], msg[5])
            return resposta
        
