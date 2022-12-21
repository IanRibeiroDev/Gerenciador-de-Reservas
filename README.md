# Documentação  - Sistema de reservas GAI (Doc em construção)

___**Equipe:**___ Amanda Araújo, George Lima e Ian Ribeiro.

___**Disciplinas envolvidas:**___
Estruturas de Dados, Sistemas Operacionais, Protocolos de Intercomunicação de Redes de Computadores.

**Requisitos por disciplina:**

___**ED:**___ Estruturas de dados lineares e não-lineares, métodos autorais, encapsulamento, tratamento de exceções e interação programa-usuário.

___**SO:**___ Uso de sockets, threads e semáforos.

___**PIRC:**___ Protocolo de transporte (TCP/UDP) e Protocolo de aplicação (podendo ser autoral).



**Estruturas de Dados utilizadas:**

___**Lista sequencial**___ para armazenas anos,

___**Lista encadeada**___ para armazenar meses,

___**Árvore AVL**___ para armazenar as tabelas de reservas separadas por dia,

___**Tabela Hash**___ para armazenar as reservas (nome e cpf como chave e reservas como valores).


**Protocolos utilizados:**

___**Camada de transporte:**___ UDP,

___**Camada de aplicação:**___ Protocolo autoral (detalhado adiante).


**Protocolo autoral de aplicação:**

Comandos disponíveis:

___**'NEW'**___ = Cliente deseja efetuar uma nova reserva. Chama o método inicial correspondente a esta operação.

___**'LIST'**___ = Cliente deseja listar as reservas já efetuadas. Chama o método inicial correspondente a esta operação.

___**'DEL'**___ = Cliente deseja excluir uma reserva já efetuada por ele. Chama o método inicial correspondente.


**Lista de Status:**

São enviados junto às mensagens para indicar o resultado da solicitação. Serve para controle interno e não são exibidos no terminal do cliente.

Tabela de códigos:

___**100**___ = Indica que a solicitação foi bem sucedida;

___**200**___ = Erro: Não há mais mesas disponíveis na data solicitada;

___**201**___ = Erro: Mesa selecionada reservada por outro cliente

