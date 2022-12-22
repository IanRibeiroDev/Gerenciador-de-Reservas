# Documentação  - Sistema de reservas GAIA (Versão Beta 1.0) #

___**Equipe:**___ Amanda Cruz de Araújo, George Lima e Ian Ribeiro.

___**Disciplinas envolvidas:**___
Estruturas de Dados, Sistemas Operacionais, Protocolos de Intercomunicação de Redes de Computadores.

**Requisitos por disciplina:**

___**ED:**___ Estruturas de dados lineares e não-lineares, métodos autorais, encapsulamento, tratamento de exceções e interação programa-usuário.

___**SO:**___ Uso de sockets, threads e semáforos.

___**PIRC:**___ Protocolo de transporte (TCP/UDP) e Protocolo de aplicação (podendo ser autoral).



**Estruturas de Dados utilizadas:**

___**Lista sequencial**___: 

Para armazenas anos, onde cada ano aponta para o gerenciador de reservas daquele ano. 

Para armazenar meses, onde cada mês aponta para a AVL de dias daquele mês.



___**Lista encadeada**___:

Para armazenar a relação de mesas disponíveis.



___**Árvore AVL**___:

Para armazenar as tabelas hash de reservas separadas por dia.



___**Tabela Hash**___:

 Para armazenar as reservas (nome e cpf como chave e reservas como valores) --> Ex: ('George:20123659874':15) --> 'George:20123659874' é a chave. 15 é o valor (mesa reservada).
 
 Os índices onde se encontram anos específicos da lista de anos. --> Ex: (2022:1) --> 2022 é a chave, que é o ano que queremos acessar. 0 é o valor, que o índice que esse ano se encontra na lista.

As operações possíveis que o cliente pode requisitar ao servidor.



**Protocolos utilizados:**

___**Camada de transporte:**___ UDP,

___**Camada de aplicação:**___ Protocolo autoral (detalhado adiante).



**Protocolo autoral de aplicação:**

Comandos disponíveis:

___**'NEW'**___ = Cliente deseja efetuar uma nova reserva. Chama o método inicial correspondente a esta operação.

___**'LIST'**___ = Cliente deseja listar as reservas já efetuadas. Chama o método inicial correspondente a esta operação.

___**'DEL'**___ = Cliente deseja excluir uma reserva já efetuada por ele. Chama o método inicial correspondente.


**Lista de Status:**

São enviados junto às mensagens no sentido servidor - cliente para indicar o resultado da solicitação. Serve para controle interno e não são exibidos no terminal do cliente.


Tabela de códigos:

___**100**___ = Indica que a solicitação foi bem sucedida;

___**200**___ = Erro: Não há mais mesas disponíveis na data solicitada;

___**201**___ = Erro: Mesa selecionada reservada por outro cliente;

___**202**___ = Erro: Não há reservas salvas no servidor efetuadas pelo cliente;

___**203**___ = Erro: Cliente já possui reserva nesse dia;


