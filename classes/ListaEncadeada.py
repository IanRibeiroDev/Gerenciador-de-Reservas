'''
Olá, Ian falando aqui!

Essa classe foi adicionada ao projeto há um mês atrás, pouco depois dos requisitos do mesmo serem anunciados.

Eu não tinha etendido que iríamos poder utilizar as classes de estruturas de dados implementadas pelo professor em aula.

Então como estávamos planejando utilizar lista encadeada no projeto, para adiantar, implementei esse código do início ao fim
quando criei o repositório.

Os métodos que acabaram sendo utilizados foram os:

insereInicio() --> Linha 151
insereFim() --> Linha 174
stringify() --> Linha 222
busca() --> Linha 64
remover() --> Linha 126
'''


from classes.Nodes import NodeLista

class ListaEncadeadaException(Exception):
    def __init__(self, erro):
        super().__init__(erro)


class ListaEncadeada:
    def __init__(self, carga:any = None):
        if carga != None:
            self.__head = NodeLista(carga)
            self.__tamanho = 1

        else:
            self.__head = None
            self.__tamanho = 0


    def estaVazia(self):
        return self.__tamanho == 0


    def tamanho(self):
        return self.__tamanho
        

    def elemento(self, posição:int): # Retorna a carga do node que se encontra na posição indicada.
        if self.estaVazia():
            raise ListaEncadeadaException('Lista vazia!')

        if posição < 1 or posição > self.__tamanho:
            raise ListaEncadeadaException(f'Informe uma posição válida entre 1 e {self.__tamanho}.')

        cursor = self.__head
        contador = 1

        while contador != posição:
            cursor = cursor.prox
            contador += 1

        return cursor.carga


    def busca(self, valor:any): # Retorna a posição em que o valor se encontra na lista.
        if self.estaVazia():
            raise ListaEncadeadaException('Lista vazia!')

        cursor = self.__head
        posição = 1

        while cursor != None:
            if cursor.carga == valor:
                return posição

            cursor = cursor.prox
            posição += 1

        raise ListaEncadeadaException('O valor não se encontra na lista!')


    def modificar(self, posição:int, novoValor:any):
        if self.estaVazia():
            raise ListaEncadeadaException('Lista vazia!')

        if posição < 1 or posição > self.__tamanho:
            raise ListaEncadeadaException(f'Informe uma posição válida entre 1 e {self.__tamanho}.')

        cursor = self.__head
        contador = 1

        while contador != posição:
            cursor = cursor.prox
            contador += 1

        cursor.carga = novoValor


    def inserir(self, posição:int, valor:any):
        if posição < 1 or posição > self.__tamanho + 1:
            raise ListaEncadeadaException(f'Informe uma posição válida entre 1 e {self.__tamanho + 1}.')

        novoNode = NodeLista(valor)

        if self.estaVazia():
            self.__head = novoNode
            self.__tamanho += 1

        elif posição == 1:
            novoNode.prox = self.__head
            self.__head = novoNode
            self.__tamanho += 1

        else:
            cursor = self.__head
            contador = 1

            while contador != posição - 1:
                cursor = cursor.prox
                contador += 1

            novoNode.prox = cursor.prox
            cursor.prox = novoNode
            self.__tamanho += 1


    def remover(self, posição:int):
        if self.estaVazia():
            raise ListaEncadeadaException('Lista vazia!')

        if posição < 1 or posição > self.__tamanho:
            raise ListaEncadeadaException(f'Informe uma posição válida entre 1 e {self.__tamanho}.')

        if posição == 1:
            antigo = self.__head
            self.__head = self.__head.prox
            antigo.prox = None
            self.__tamanho -= 1

        else:
            cursor = self.__head
            contador = 1

            while contador != posição:
                anterior = cursor
                cursor = cursor.prox
                contador += 1

            anterior.prox = cursor.prox
            cursor.prox = None
            self.__tamanho -= 1
            #return cursor.carga
            

    def insereInicio(self, valor:any):
        novoNode = NodeLista(valor)

        if self.estaVazia():
            self.__head = novoNode
            self.__tamanho += 1

        else:
            novoNode.prox = self.__head
            self.__head = novoNode
            self.__tamanho += 1


    def removeInicio(self):
        if self.estaVazia():
            raise ListaEncadeadaException('Lista vazia!')

        antigo = self.__head
        self.__head = self.__head.prox
        antigo.prox = None
        self.__tamanho -= 1


    def insereFim(self, valor:any):
        novoNode = NodeLista(valor)
        
        if self.estaVazia():
            self.__head = novoNode
            self.__tamanho += 1
        
        else:
            cursor = self.__head

            for i in range(self.__tamanho - 1):
                cursor = cursor.prox

            cursor.prox = novoNode
            self.__tamanho += 1


    def removeFim(self):
        if self.estaVazia():
            raise ListaEncadeadaException('Lista vazia!')

        if self.__tamanho == 1:
            self.__head = None
            self.__tamanho -= 1

        else:
            cursor = self.__head

            for i in range(self.__tamanho - 2):
                cursor = cursor.prox

            cursor.prox = None
            self.__tamanho -= 1


    def concatenar(self, lista2):
        listaConcatenada = ListaEncadeada()

        for i in range(self.__tamanho):
            listaConcatenada.insereFim(self.elemento(i + 1))

        for i in range(lista2.tamanho()):
            listaConcatenada.insereFim(lista2.elemento(i + 1))

        return listaConcatenada

    # Retorna todo conteúdo da lista já formatado de acordo com o protocolo de aplicação.
    def stringify(self) -> str:
        listaStr = ''

        cursor = self.__head

        while cursor != None:
            listaStr += (str(cursor.carga) + '-')
            cursor = cursor.prox

        return listaStr


    def __str__(self) -> str:
        listaStr = '[ '

        cursor = self.__head

        while cursor != None:
            listaStr += (str(cursor.carga) + ' ')
            cursor = cursor.prox

        listaStr += ']'

        return listaStr


    def __len__(self) -> int:
        return self.__tamanho
