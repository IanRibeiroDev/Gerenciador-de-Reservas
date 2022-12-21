from classes.ListaSequencial import ListaSequencial
from classes.ListaEncadeada import ListaEncadeada
from classes.ChainingHashTable import ChainingHashTable
from classes.GerenciadorReservas import GerenciadorReservas
import datetime

'''
Cada indice de self.__anos aponta para o gerenciador de reservas daquele ano.
self.__indiceAnos guarda em que indice cada ano esta presente dentro da lista.

Basicamente:

self.__anos = [2022, 2023, 2024] --> Onde 2022 = objeto GerenciadorReservas() de 2022

self.__indiceAnos = {
    2022:0,
    2023:1,
    2024:2
}  -----------> A chave ano leva para qual indice de self.__anos aquele ano está armazenado. Ex: 2022 se encontra em self.__anos[0].
'''

class GerenciadorClientes:
    def __init__(self) -> None:
        self.__anos = ListaSequencial()
        self.__indiceAnos = ChainingHashTable(3)
        self.__inserirAnos()
        

    # Insere o ano atual e os 2 próximos anos em self.__anos.
    # Guarda a informação de em quais índices foram inseridos em self.__indiceAnos.
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
            # Parte 1
            if msg[2] == '<1>':  
                # Cria variáveis para melhor legibilidade do código.
                ano = int(msg[4])
                mes = int(msg[5])            
                dia = int(msg[6])
                
                # Verifica quais as mesas disponíveis e retorna para o cliente essa informação.
                resposta = self.__getMesasDisponiveis(ano, mes, dia)
                return resposta

            # Parte 2
            elif msg[2] == '<2>':
                # Cria variáveis para melhor legibilidade do código.
                ano = int(msg[4])
                mes = int(msg[5])            
                dia = int(msg[6])
                mesa = int(msg[7])
                cliente = msg[3]

                # Verifica se a mesa escolhida ainda se encontra disponível.
                mesasDisponiveis = self.__getMesasDisponiveis(ano, mes, dia).removeprefix('100-OK-')


                # Se a mesa ainda está disponível, adiciona a reserva.
                if str(mesa) in mesasDisponiveis.split('-'):
                    resposta = self.__adicionarReserva(ano, mes, dia, mesa, cliente)
                    return resposta
                
                # Se acabaram as mesas nesse íterim.
                elif mesasDisponiveis.split('-')[0] == '200':
                    resposta = mesasDisponiveis
                    return resposta

                # Se alguem ja reservou nesse íterim.
                resposta = f'201-ERR-NotAvailable-{mesasDisponiveis}'
                return resposta
            
                
    # Seleciona o gerenciador de reservas responsável pelo ano requisitado e pede para que retorne as mesas disponíveis.
    def __getMesasDisponiveis(self, ano:int, mes:int, dia:int):
            indiceAno = self.__indiceAnos.get(ano)
            gerenciadorReservas = self.__anos.elemento(indiceAno)

            mesasDisponiveis = gerenciadorReservas.verificarMesasDisponiveis(mes, dia)

            if mesasDisponiveis == '':
                resposta = '200-ERR-EmptyList'
                return resposta

            resposta = f'100-OK-{mesasDisponiveis}'
            return resposta


    # Seleciona o gerenciador de reservas responsável pelo ano requisitado e pede para que adicione uma reserva..
    def __adicionarReserva(self, ano:int, mes:int, dia:int, mesa:int, cliente:str):
        indiceAno = self.__indiceAnos.get(ano)
        gerenciadorReservas = self.__anos.elemento(indiceAno)

        gerenciadorReservas.insereReserva(mes, dia, mesa ,cliente)

        return '100-OK-InsertSucess'

