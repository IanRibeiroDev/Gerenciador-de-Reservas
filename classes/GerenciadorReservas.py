from classes.ListaSequencial import ListaSequencial
from classes.ListaEncadeada import ListaEncadeada
from classes.ArvoreAVL import AVLTree
from classes.ChainingHashTable import ChainingHashTable, AbsentKeyException
from threading import Semaphore

'''
Cada indice de self.__meses aponta para a AVL de dias daquele mês.
O valor dos nodes dessas AVLs são Hash Tables que armazenam pares (chave:valor) de (NomeCliente+cpfCliente:MesaReservada)

Na HashTable também é armazenada uma Lista Encadeada contendo todas as mesas disponíveis daquele dia específico.
Toda vez que uma reserva é feita ou removida, a mesa é inserida de volta ou removida da lista de mesas disponíveis.

Na HashTable também é armazenado o valor do dia que ela está representando, o qual é utilizado nos métodos de comparação:
__eq__, __lt__ e __gt__ para comparar esta com outras Hash Tables que também estão representando dias.

Caso alguma das Hash Tables não possua esse valor inserido, o método de comparação default é comparar os seus tamanhos.
'''

class GerenciadorReservas:
    def __init__(self, ano:int):
        self.__ano = ano
        self.__meses = ListaSequencial()
        self.__mutex = Semaphore()

        # Cria uma AVL de dias para cada mês.
        for i in range(1, 13):
            dias = AVLTree()
            self.__meses.inserir(i, dias)


    # Recupera a lista de mesas disponiveis de um dia específico.
    def verificarMesasDisponiveis(self, mes:int, dia:int):
        # Recupera a AVL de dias e acessa a HashTable contida nela.  
        self.__mutex.acquire()

        arvoreDias = self.__meses.elemento(mes)
        hashTableReservas = arvoreDias.getNodeValue(dia)
        

        # Se o node do dia ainda não tiver sido criado, o cria, e acessa sua HashTable.
        if hashTableReservas == None:
            self.__addDia(arvoreDias, dia)
            hashTableReservas = arvoreDias.getNodeValue(dia)


        # Acessa a lista de mesas disponíveis e retorna todo o conteúdo dela já formatada para ser enviada pelo protocolo.
        listaDisponiveis = hashTableReservas.get('Mesas Disponiveis')
        protocoloMesasDisponiveis = listaDisponiveis.stringify()

        self.__mutex.release()
        return protocoloMesasDisponiveis




    # Adiciona um node da AVL com uma HashTable representando um dia.
    def __addDia(self, arvore:AVLTree, dia:int):
        hashTableReservas = self.__createHashTable(dia)
        arvore.insert(hashTableReservas)
        

    # Cria HashTable onde ficarão armazenadas as reservas.
    # Automaticamente adiciona nela lista de mesas disponíveis desse dia, e o dia que ela vai representar.
    def __createHashTable(self, dia:int, size:int = 30) -> ChainingHashTable:
        hashTableReservas = ChainingHashTable(size)
        hashTableReservas.put('dia representado', dia)

        listaDisponiveis = ListaEncadeada()
        for i in range (1, size + 1):
            listaDisponiveis.insereFim(i)

        hashTableReservas.put('Mesas Disponiveis', listaDisponiveis)
        return hashTableReservas




    # Método para inserção de reservas na Hash Table.
    def insereReserva(self, mes:int, dia:int, mesa:int, cliente:str):
        # Recupera a AVL de dias e acessa a HashTable contida nela, depois insere a reserva do cliente na HashTable.
        self.__mutex.acquire()

        arvoreDias = self.__meses.elemento(mes)
        hashTableReservas = arvoreDias.getNodeValue(dia)

        # Se o cliente já tem uma reserva, náo permite reservar novamente. Ele deve deletar a reserva antes.
        try:
            hashTableReservas.get(cliente)

            self.__mutex.release()
            return '203-ERR-AlreadyHasReservation'

        # Caso náo tenha reserva no dia ainda, insere reserva.
        except AbsentKeyException:
            hashTableReservas.put(cliente, mesa)
            
            # Remove a mesa que acabou de ser reservada da lista de mesas disponíveis.
            listaDisponiveis = hashTableReservas.get('Mesas Disponiveis')    
            posicao = listaDisponiveis.busca(mesa)
            listaDisponiveis.remover(posicao)

            self.__mutex.release()
            return '100-OK-InsertSucess'



    # Lista todas as reservas que o cliente fez no mês.
    def listarReservasMes(self, mes:int, cliente:str, suffix:bool = False):
        arvoreDias = self.__meses.elemento(mes)

        # Recebe uma string com todos os dias já inseridos na AVL.
        diasInseridos = arvoreDias.stringDias() 
        
        ponteiro = 0
        reservasCliente = ''

        # Procura reservas feitas pelo cliente em cada dia.
        while ponteiro < len(diasInseridos):
            # Caso seja um dia de 2 dígitos.
            if diasInseridos[ponteiro + 1] != ' ':
                dia = int(diasInseridos[ponteiro] + diasInseridos[ponteiro + 1])
                hashTableReservas = arvoreDias.getNodeValue(dia)
                ponteiro += 3

            # Caso seja um dia de 1 dígito.
            else:
                dia = int(diasInseridos[ponteiro])
                hashTableReservas = arvoreDias.getNodeValue(dia)
                ponteiro += 2

            # Tenta pegar a reserva e adicionála a string, caso falha, simplesmente continua.
            try:
                mesa = hashTableReservas.get(cliente)
                reservasCliente += f'{self.__ano}:{mes}:{dia}:{mesa}-'
            except AbsentKeyException:
                continue

        if not suffix:
            return reservasCliente.removesuffix('-')

        return reservasCliente


    # Lista todas as reservas que o cliente fez no ano.
    def listarReservasAno(self, cliente:str):
        reservasCliente = ''

        for i in range(1, 13):
            reservasCliente += self.listarReservasMes(i, cliente, True)

        return reservasCliente


    def removeReserva(self, mes:int, dia:int, cliente:str):
        self.__mutex.acquire()

        arvoreDias = self.__meses.elemento(mes)
        hashTableReservas = arvoreDias.getNodeValue(dia)

        
        entry = hashTableReservas.remove(cliente)

        listaDisponiveis = hashTableReservas.get('Mesas Disponiveis')
        listaDisponiveis.insereInicio(entry.value)

        self.__mutex.release()
        


# Fiquem a vontade para usar esses exemplos para entender melhor como a estrutura de dados funciona.
# Lembrar de remover o "classes." dos imports, se não, acontece um erro. Nunca conseguimos descobrir o porquê.
if __name__ == '__main__':

    a = GerenciadorReservas(2023)

    for i in range(1, 13):
        a.verificarMesasDisponiveis(i, 1)
        a.verificarMesasDisponiveis(i, 5)
        a.verificarMesasDisponiveis(i, 16)
        a.verificarMesasDisponiveis(i, 28)
        a.verificarMesasDisponiveis(i, 4)

    for i in range(1, 13):
        a.insereReserva(i, 1, 29, 'Ian Ribeiro de Mendonça')
        a.insereReserva(i, 5, 2, 'Ian Ribeiro de Mendonça')
        a.insereReserva(i, 16, 25, 'George')
        a.insereReserva(i, 28, 19, 'Ian Ribeiro de Mendonça')
        a.insereReserva(i, 28, 17, 'Amanda')
        a.insereReserva(i, 5, 7, 'Amanda')
        a.insereReserva(i, 4, 24, 'George')
        a.insereReserva(i, 28, 23, 'George')

    reservasIan = a.listarReservasAno('Ian Ribeiro de Mendonça')
    reservasAmanda = a.listarReservasAno('Amanda')
    reservasGeorge = a.listarReservasAno('George')

    splitIan = reservasIan.split('-')
    splitGeorge = reservasGeorge.split('-')
    splitAmanda = reservasAmanda.split('-')

    fevereiroIan = a.listarReservasMes(2, 'Ian Ribeiro de Mendonça')
    print(fevereiroIan)
    print()

    a.removeReserva(2, 28, 'Ian Ribeiro de Mendonça')
    
    fevereiroIan = a.listarReservasMes(2, 'Ian Ribeiro de Mendonça')
    print(fevereiroIan)
    print()

    a.removeReserva(2, 28, 'Ian Ribeiro de Mendonça')

    print('Ian: ', splitIan)
    print()
    print('Amanda: ', splitAmanda)
    print()
    print('George: ', splitGeorge)
