# Documentação - Gerenciador de Reservas

## Equipe
 - Amanda Cruz de Araújo; 
 - George Barbosa de Lima;
 - Ian Ribeiro de Mendonça.

## Disciplinas Envolvidas
Estruturas de Dados (ED), Sistemas Operacionais (SO), Protocolos de Intercomunicação de Redes de Computadores (PIRC).

## Requisitos por Disciplina:

___**ED:**___ Estruturas de dados lineares e não-lineares, métodos autorais, encapsulamento, tratamento de exceções e interação programa-usuário.

___**SO:**___ Uso de sockets, threads e semáforos.

___**PIRC:**___ Protocolo de transporte (TCP/UDP) e Protocolo de aplicação (podendo ser autoral).



## Estruturas de Dados Utilizadas

___**Lista sequencial**___: 

- Para armazenas anos, onde cada ano aponta para o gerenciador de reservas daquele ano. 

- Para armazenar meses, onde cada mês aponta para a AVL de dias daquele mês.


___**Lista encadeada**___:

- Para armazenar a relação de mesas disponíveis.


___**Árvore AVL**___:

- Para armazenar as tabelas hash de reservas separadas por dia.


___**Tabela Hash**___:

- Para armazenar as reservas (nome e cpf como chave e reservas como valores) --> Ex: ('George:20123659874':15) --> 'George:20123659874' é a chave. 15 é o valor (mesa reservada).

- Armazenar a lista encadeada de mesas disponíveis de cada dia, a qual a chave é "Mesas Disponiveis".

- A posição onde se encontram anos específicos da lista de anos. --> Ex: (2022:1) --> 2022 é a chave, que é o ano que queremos acessar. 1 é o valor, da posição onde esse ano se encontra na lista.

- As operações possíveis que o cliente pode requisitar ao servidor.



## Protocolos Utilizados

___**Camada de transporte:**___ UDP.

___**Camada de aplicação:**___ Protocolo autoral (detalhado adiante).



## Protocolo Autoral de Aplicação

**Comandos disponíveis:**

- ___**'NEW'**___ - Cliente deseja efetuar uma nova reserva.

- ___**'LIST'**___ - Cliente deseja listar as reservas já efetuadas.

- ___**'DEL'**___ - Cliente deseja excluir uma reserva já efetuada por ele.


**Status:**

São enviados junto às mensagens no sentido servidor - cliente para indicar o resultado da solicitação. Serve para controle interno e não são exibidos no terminal do cliente.


Tabela de status:

- ___**100**___ - Indica que a solicitação foi bem sucedida;

- ___**200**___ - Erro: Não há mais mesas disponíveis na data solicitada;

- ___**201**___ - Erro: Mesa selecionada reservada por outro cliente;

- ___**202**___ - Erro: Não há reservas efetuadas pelo cliente salvas no servidor;

- ___**203**___ - Erro: Cliente já possui reserva nesse dia.


**Comandos enviados em cada transação:**

- Quando uma nova reserva é solicitada:

    - Cliente: CLI-NEW-<1>-NomeCliente-Ano-Mes-Dia
    - Servidor: 100-OK-2-3-4-5-6-...(todas as mesas disponiveis)

    - Cliente: CLI-NEW-<2>-NomeCliente-Ano-Mes-Dia-Mesa
    - Servidor: 100-OK

- Quando a lista de todas as reservas efetuadas pelo cliente é solicitada:

    - Cliente: CLI-LIST-<1>-NomeCliente
    - Servidor: 100-OK-2023:2:4:29-2023...(ANO:MES:DIA:MESA-)

- Quando a deleção de uma reserva é solicitada:

    - Primeiro é solicitado ao servidor a lista de reservas efetuadas pelo cliente, logo, os comandos de listagem são trocados. Após o cliente escolher qual reserva quer deletar:

        - Cliente: CLI-DEL-<1>-NomeCliente-Ano-Mes-Dia
        - Servidor: 100+OK

- Em caso de erro, é enviado pelo servidor:

    - 200-ERR-EmptyList
    - 201-ERR-NotAvailable-4-5-6-...(todas as mesas disponiveis)
    - 202-ERR-NoReservations
    - 203-ERR-AlreadyHasReservation


## Sistemas Operacionais

Servidor é aberto na porta 60000.

É multithread, podendo receber requisições de vários clientes ao mesmo tempo.

Para não sobrecarregar a memória, foi desenvolvido um sistema onde os nós da árvore AVL são criados de acordo com a necessidade. Quando um cliente envia uma requisição de uma reserva, é checado se o nó, que representa o dia no qual ele deseja fazer a reserva, já existe. Caso não exista, ele é imediatamente criado, já inserindo a hash table onde ficarão salvas as reservas nele.

Há semáforos bloqueando regiões críticas, prevenindo que mais de um cliente consiga reservar a mesma mesa, ou que mais de um nó na árvore seja criado para o mesmo dia.