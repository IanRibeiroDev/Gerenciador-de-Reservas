from ListaSequencial import ListaSequencial
from ListaEncadeada import ListaEncadeada
from ArvoreAVL import AVLTree
from ChainingHashTable import AbsentKeyException

class GerenciadorReservas:
    def __init__(self, ano:int):
        self.__ano = ano
        self.__meses = ListaSequencial()

        # Cria uma AVL de dias para cada mês.
        for i in range(1, 13):
            dias = AVLTree()
            self.__meses.inserir(i, dias)


    def verificarMesasDisponiveis(self, mes:int, dia:int):
        # Recupera a AVL de dias e acessa a HashTable contida nela. 
        arvoreDias = self.__meses.elemento(mes)
        hashTableReservas = arvoreDias.getHashNode(dia)
        
        # Se o node do dia ainda não tiver sido criado, o cria, e acessa sua HashTable.
        if hashTableReservas == None:
            self.__addDia(arvoreDias, dia)
            hashTableReservas = arvoreDias.getHashNode(dia)

        # Acessa a lista de mesas disponíveis e retorna todo o conteúdo dela já formatada para ser enviada pelo protocolo.
        listaDisponiveis = hashTableReservas.get('Mesas Disponiveis')
        return listaDisponiveis.stringify()


    # Adiciona um node representando um dia do mês na AVL.
    def __addDia(self, arvore:AVLTree, dia:int):
        arvore.insertHashNode(dia)
        self.__addListaDisponiveis(arvore, dia)

    # Adiciona a lista de mesas disponíveis a HashTable do node recém criado.
    def __addListaDisponiveis(self, arvore:AVLTree, dia:int):
        hashTable = arvore.getHashNode(dia)

        listaDisponiveis = ListaEncadeada()
        for i in range (1, hashTable.size + 1):
            listaDisponiveis.insereFim(i)

        hashTable.put('Mesas Disponiveis', listaDisponiveis)


    def insereReserva(self, mes:int, dia:int, mesa:int, nomeCliente:str):
        # Recupera a AVL de dias e acessa a HashTable contida nela, depois insere a reserva do cliente na HashTable.
        arvoreDias = self.__meses.elemento(mes)
        hashTableReservas = arvoreDias.getHashNode(dia)
        hashTableReservas.put(nomeCliente, mesa)
        
        # Remove a mesa que acabou de ser reservada da lista de mesas disponíveis.
        listaDisponiveis = hashTableReservas.get('Mesas Disponiveis')    
        posicao = listaDisponiveis.busca(mesa)
        listaDisponiveis.remover(posicao)


    # Lista todas as reservas que o cliente fez no mês.
    def listarReservasMes(self, mes:int, nomeCliente:str, suffix:bool = False):
        arvoreDias = self.__meses.elemento(mes)

        # Recebe uma string com todos os dias já inseridos na AVL.
        diasInseridos = arvoreDias.emOrdem(False) 
        
        ponteiro = 0
        reservasCliente = ''

        while ponteiro < len(diasInseridos):
            # Caso seja um dia de 2 dígitos.
            if diasInseridos[ponteiro + 1] != ' ':
                dia = int(diasInseridos[ponteiro] + diasInseridos[ponteiro + 1])
                hashTableReservas = arvoreDias.getHashNode(dia)
                ponteiro += 3

            # Caso seja um dia de 1 dígito.
            else:
                dia = int(diasInseridos[ponteiro])
                hashTableReservas = arvoreDias.getHashNode(dia)
                ponteiro += 2

            try:
                mesa = hashTableReservas.get(nomeCliente)
                reservasCliente += f'{self.__ano}:{mes}:{dia}:{mesa}-'
            except AbsentKeyException:
                continue

        if not suffix:
            return reservasCliente.removesuffix('-')

        return reservasCliente


    def listarReservasAno(self, nomeCliente:str):
        reservasCliente = ''

        for i in range(1, 13):
            reservasCliente += self.listarReservasMes(i, nomeCliente, True)

        return reservasCliente.removesuffix('-')


    def removeReserva(self, mes:int, dia:int, nomeCliente:str):
        arvoreDias = self.__meses.elemento(mes)
        hashTableReservas = arvoreDias.getHashNode(dia)

        try:
            entry = hashTableReservas.remove(nomeCliente)
        except AbsentKeyException:
            return '400+ERR'

        listaDisponiveis = hashTableReservas.get('Mesas Disponiveis')
        listaDisponiveis.insereInicio(entry.value)


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

    
'''
    for i in range(1, 13):
        reservasCliente = a.listarReservas(i,'Ian Ribeiro de Mendonça')
        reservasCliente2 = a.listarReservas(i,'Amanda')
        reservasCliente3 = a.listarReservas(i,'George')

        print('Reservas Ian Mes', str(i), ': ', reservasCliente)
        print('Reservas Amanda Mes', str(i), ': ', reservasCliente2)
        print('Reservas George Mes', str(i), ': ', reservasCliente3)

    reservasAno = ''
    for i in range(1, 13):
        reservasAno += a.listarReservas(i, 'Amanda')

    print('Reservas do ano inteiro de Amanda: ', reservasAno)
'''

