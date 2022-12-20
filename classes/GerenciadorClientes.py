from classes.ListaSequencial import ListaSequencial
from classes.ListaEncadeada import ListaEncadeada
from classes.ChainingHashTable import ChainingHashTable
from classes.GerenciadorReservas import GerenciadorReservas
import datetime

class GerenciadorClientes:
    #controlID = 0

    def __init__(self) -> None:
        self.__anos = ListaSequencial()
        self.__anosPassados = ListaEncadeada()
        self.__indiceAnos = ChainingHashTable(3)
        self.__inserirAnos()
        #self.__ID = self.__class__.controlID + 1
        #self.__class__.controlID += 1
        


    def __inserirAnos(self):
        dataAtual = datetime.date.today()
        contador = 0

        while contador < 3:
            ano = dataAtual.year + contador
            indice = contador + 1

            gerenciadorAno = GerenciadorReservas(ano)
            self.__anos.inserir(indice, gerenciadorAno)
            self.__indiceAnos.put(ano, indice)
            contador += 1




    # Redireciona para o método apropriado de acordo com o conteúdo da mensagem
    # <1> == parte 1
    # <2> == parte 2 e assim vai
    def handleMsg(self, msg):
        # Adicionar nova reserva.
        if msg[1] == 'NEW':  
            if msg[2] == '<1>':  
                ano = int(msg[4])
                mes = int(msg[5])            
                dia = int(msg[6])
                
                resposta = self.__getMesasDisponiveis(ano, mes, dia)
                return resposta

            elif msg[2] == '<2>':
                ano = int(msg[4])
                mes = int(msg[5])            
                dia = int(msg[6])
                mesa = int(msg[7])
                nomeCliente = msg[3]

                mesasDisponiveis = self.__getMesasDisponiveis(ano, mes, dia).removeprefix('100-OK-')


                # Se a mesa ainda está disponível.
                if str(mesa) in mesasDisponiveis.split('-'):
                    resposta = self.__adicionarReserva(ano, mes, dia, mesa, nomeCliente)
                    return resposta
                
                # Se acabaram as mesas nesse íterim.
                elif mesasDisponiveis.split('-')[0] == '200':
                    resposta = mesasDisponiveis
                    return resposta

                # Se alguem ja reservou.
                resposta = f'201-ERR-NotAvailable-{mesasDisponiveis}'
                return resposta
            
                

    def __getMesasDisponiveis(self, ano:int, mes:int, dia:int):
            indiceAno = self.__indiceAnos.get(ano)
            gerenciadorReservas = self.__anos.elemento(indiceAno)

            mesasDisponiveis = gerenciadorReservas.verificarMesasDisponiveis(mes, dia)

            if mesasDisponiveis == '':
                resposta = '200-ERR-EmptyList'
                return resposta

            resposta = f'100-OK-{mesasDisponiveis}'
            return resposta



    def __adicionarReserva(self, ano:int, mes:int, dia:int, mesa:int, nomeCliente:str):
        indiceAno = self.__indiceAnos.get(ano)
        gerenciadorReservas = self.__anos.elemento(indiceAno)

        gerenciadorReservas.insereReserva(mes, dia, mesa ,nomeCliente)

        return '100-OK-InsertSucess'

