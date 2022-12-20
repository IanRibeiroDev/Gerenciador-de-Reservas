import socket
import time
import datetime

# Verifica se a data que o usuário inseriu é uma data válida.
def validaData(data:str) -> bool:
    try:
        data = data.split('/')

        if len(data) != 3:
            raise ValueError('Formato inválido, lembre-se de inserir a data no formato dia/mês/ano. Ex: 05/12/2023')
            
        dia = int(data[0])
        mes = int(data[1])
        ano = int(data[2])
        dataAtual = datetime.date.today()


        # Verifica se o ano é válido.
        if ano not in [dataAtual.year, dataAtual.year + 1, dataAtual.year + 2]:
            raise ValueError(f'Informe um ano válido entre {dataAtual.year}-{dataAtual.year + 2}.')


        # Verifica, caso o ano seja o atual, se o usuário não digitou um mês que já passou. 
        if ano == dataAtual.year:
            if mes < dataAtual.month or mes > 12:
                if dataAtual.month == 12:
                    raise ValueError(f'O único mês válido para esse ano é {dataAtual.month}.')
                else:
                    raise ValueError(f'Informe um mês válido entre {dataAtual.month}-{12}.')

        # Se não, verifica apenas se o mês é válido.
        else:
            if mes < 1 or mes > 12:
                    raise ValueError(f'Informe um mês válido entre {1}-{12}.')


        # Verificação se o mês é Fevereiro.
        if mes == 2:
            # Verifica, caso o mês seja o atual, se o usuário não digitou um dia que já passou. 
            if ano == dataAtual.year:
                if mes == dataAtual.month:
                    if dia < dataAtual.day or dia > 28:
                        if dataAtual.day == 28:
                            raise ValueError(f'O único dia válido para esse mês é {dataAtual.day}.')
                        else:
                            raise ValueError(f'Informe um dia válido entre {dataAtual.day}-{28}.')

            # Se não, verifica apenas se o dia é válido.
            else:
                if dia < 1 or dia > 28:
                    raise ValueError(f'Informe um dia válido entre {1}-{28}.')
            

        # Verifica se o mês tem 31 dias.
        elif mes in [1, 3, 5, 7, 8, 10, 12]:
            # Verifica, caso o mês seja o atual, se o usuário não digitou um dia que já passou. 
            if ano == dataAtual.year:
                if mes == dataAtual.month:
                    if dia < dataAtual.day or dia > 31:
                        if dataAtual.day == 31:
                            raise ValueError(f'O único dia válido para esse mês é {dataAtual.day}.')
                        else:
                            raise ValueError(f'Informe um dia válido entre {dataAtual.day}-{31}.')

            # Se não, verifica apenas se o dia é válido.
            else:
                if dia < 1 or dia > 31:
                    raise ValueError(f'Informe um dia válido entre {1}-{31}.')


        # Se não entrou nos outros laços, então o mês tem 30 dias.
        else:
            # Verifica, caso o mês seja o atual, se o usuário não digitou um dia que já passou. 
            if ano == dataAtual.year:
                if mes == dataAtual.month:
                    if dia < dataAtual.day or dia > 30:
                        if dataAtual.day == 30:
                            raise ValueError(f'O único dia válido para esse mês é {dataAtual.day}.')
                        else:
                            raise ValueError(f'Informe um dia válido entre {dataAtual.day}-{30}.')

            # Se não, verifica apenas se o dia é válido.
            else:
                if dia < 1 or dia > 30:
                    raise ValueError(f'Informe um dia válido entre {1}-{30}.')


        return True

    except ValueError as ve:
        print(ve)
        time.sleep(3)
        return False



# Prepara a data para ser enviado na forma de comando do protocolo.
def comandoData(data:str) -> str:
    data = data.split('/')
    
    data[0] = int(data[0])
    data[1] = int(data[1])

    return f'{data[2]}-{str(data[1])}-{str(data[0])}'



# Responsável pelo trâmite do cliente escolher a mesa para reserva, e realiza todo tratamento de erros necessário.
def validaMesa(comando:str, resposta:list):
    primeiraTentativa = True
    while True:
        mesasDisponiveis = 'Mesas Disponíveis: '
        indice = 2

        if not primeiraTentativa:
            indice = 3
            comando = comando.removesuffix(f'-{mesaEscolhida}')

        for i in range(indice, len(resposta)):
            mesasDisponiveis += resposta[i] + ' '

        mesasDisponiveis = mesasDisponiveis.removesuffix(' ') + '\n'
        print(mesasDisponiveis)
        
        mesaInvalida = True
        while mesaInvalida:

            mesaEscolhida = input('Informe a mesa que deseja reservar: ')
            
            if mesaEscolhida.upper() == 'QUIT':
                print('Reserva cancelada.\n')
                time.sleep(3)
                return

            if primeiraTentativa and mesaEscolhida in resposta[2:]:
                mesaInvalida = False

            elif not primeiraTentativa and mesaEscolhida in resposta[3:]:
                mesaInvalida = False

            else:
                print('Informe uma mesa que se encontra na lista de mesas disponíveis.\n')
                time.sleep(3)

        comando += f'-{mesaEscolhida}'
        comando = comando.replace('<1>', '<2>')
        resposta = enviarParaServidor(comando)

        if resposta[0] == '100':
            print('Reserva inserida com sucesso!\n')
            time.sleep(3)
            return

        elif resposta[0] == '200':
            print('Infelizmente não há mais reservas disponíveis para esse dia.\n')
            time.sleep(3)
            return

        elif resposta[0] == '201':
            print('Infelizmente, outro cliente foi mais veloz, e efetou uma reserva nessa mesa enquanto você se decidia. Por favor escolha outra mesa para reservar. Você também pode digitar QUIT para cancelar a reserva.\n')
            time.sleep(7)
            primeiraTentativa = False



# Função a ser chamada caso o cliente queira efetuar uma nova reserva.
def novaReserva(nomeCliente:str):
    comando = f'CLI-NEW-<1>-{nomeCliente}-'
    dataValida = False

    while not dataValida:
        data = input('\nInforme a data na qual deseja realizar a reserva no formato dia/mês/ano: ')
        dataValida = validaData(data)

    comando += comandoData(data)
    resposta = enviarParaServidor(comando)

    if resposta[0] == '200':
        print('Infelizmente não há mais mesas disponíveis nesse dia.\n')
        time.sleep(3)
        return

    validaMesa(comando, resposta)
    
    

# Função para enviar o comando da requisição para o servidor. Devolve a resposta já decodificada e já feito o split.
def enviarParaServidor(comando):
    sock.sendto(comando.encode(), server_address)

    resposta, address = sock.recvfrom(1024)
    
    return resposta.decode().split('-')



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 60000)

option = ''
print('Bem-vindo ao Gerenciador de Reservas GAI!') # GAI = George Amanda Ian
nomeCliente = input('Para começar, informe seu nome: ')

while option != 's':

    print(f'\n{"OPERAÇÕES":^30}')
    print(f'{"":=^30}')
    print('(n) --> Fazer uma nova reserva')
    print('(a) --> Alterar uma reserva efetuada')
    print('(d) --> Excluir uma reserva efetuada')
    print('(l) --> Listar todas as reservas efetuadas.')
    print('(s) --> Encerrar sua conexão\n')

    option = input(f'{"DIGITE A OPÇÃO DESEJADA ":^30}\n\n{"":13}')


    # Nova reserva
    if option == 'n': 
        novaReserva(nomeCliente)

        


    