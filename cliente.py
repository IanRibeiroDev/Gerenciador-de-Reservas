import socket
import time
import datetime

def comandoData(data:str) -> str:
    data = data.split('/')
    
    data[0] = int(data[0])
    data[1] = int(data[1])

    return f'{data[2]}-{str(data[1])}-{str(data[0])}'


def validaData(data:str):
    try:
        data = data.split('/')

        if len(data) != 3:
            raise ValueError('Formato inválido, lembre-se de inserir a data no formato dia/mês/ano. Ex: 05/12/2023')
            
        dia = int(data[0])
        mes = int(data[1])
        ano = int(data[2])
        dataAtual = datetime.date.today()

        if ano not in [dataAtual.year, dataAtual.year + 1, dataAtual.year + 2]:
            raise ValueError(f'Informe um ano válido entre {dataAtual.year}-{dataAtual.year + 2}.')


        if ano == dataAtual.year:
            if mes < dataAtual.month or mes > 12:
                if dataAtual.month == 12:
                    raise ValueError(f'O único mês válido para esse ano é {dataAtual.month}.')
                else:
                    raise ValueError(f'Informe um mês válido entre {dataAtual.month}-{12}.')

        else:
            if mes < 1 or mes > 12:
                    raise ValueError(f'Informe um mês válido entre {1}-{12}.')


        # Verificação se o mês é Fevereiro.
        if mes == 2:
            if ano == dataAtual.year:
                if mes == dataAtual.month:
                    if dia < dataAtual.day or dia > 28:
                        if dataAtual.day == 28:
                            raise ValueError(f'O único dia válido para esse mês é {dataAtual.day}.')
                        else:
                            raise ValueError(f'Informe um dia válido entre {dataAtual.day}-{28}.')

            else:
                if dia < 1 or dia > 28:
                    raise ValueError(f'Informe um dia válido entre {1}-{28}.')
            

        # Verifica se o mês tem 31 dias.
        elif mes in [1, 3, 5, 7, 8, 10, 12]:
            if ano == dataAtual.year:
                if mes == dataAtual.month:
                    if dia < dataAtual.day or dia > 31:
                        if dataAtual.day == 31:
                            raise ValueError(f'O único dia válido para esse mês é {dataAtual.day}.')
                        else:
                            raise ValueError(f'Informe um dia válido entre {dataAtual.day}-{31}.')

            else:
                if dia < 1 or dia > 31:
                    raise ValueError(f'Informe um dia válido entre {1}-{31}.')


        # Se não entrou nos outros laços, então o mês tem 30 dias.
        else:
            if ano == dataAtual.year:
                if mes == dataAtual.month:
                    if dia < dataAtual.day or dia > 30:
                        if dataAtual.day == 30:
                            raise ValueError(f'O único dia válido para esse mês é {dataAtual.day}.')
                        else:
                            raise ValueError(f'Informe um dia válido entre {dataAtual.day}-{30}.')

            else:
                if dia < 1 or dia > 30:
                    raise ValueError(f'Informe um dia válido entre {1}-{30}.')

        return True

    except ValueError as ve:
        print(ve)
        time.sleep(0.1)
        return False


def enviarParaServidor(comando):
    sock.sendto(comando.encode(), server_address)

    resposta, address = sock.recvfrom(1024)
    
    return resposta.decode()


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

    if option == 'n': # Nova reserva
        comando = f'CLI-NEW-{nomeCliente}-'
        dataValida = False

        while not dataValida:
            data = input('\nInforme a data na qual deseja realizar a reserva no formato dia/mês/ano: ')
            dataValida = validaData(data)

        comando += comandoData(data)

        resposta = enviarParaServidor(comando)

        print(resposta)


    