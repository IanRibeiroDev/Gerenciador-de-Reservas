import socket
import time
import datetime
import sys

# Função responsável por verificar se o nome que o usuário inseriu é válido.
def validaNomeCliente(nomeCliente:str):
    nomeCliente = nomeCliente.split(' ')

    for i in range(len(nomeCliente)):
        if not nomeCliente[i].isalpha():
            return 'Informe um nome válido com apenas letras.\n'

    return True



# Função responsável por verificar se o CPF que o usuário inseriu é válido.
def validaCPF(CPF:str):
    if len(CPF) == 11 and CPF.isdecimal():
        return True

    return 'Informe um CPF válido de 11 dígitos com apenas números. Ex: 09845676583\n'



# Verifica se a data que o usuário inseriu é uma data válida.
def validaData(data:str) -> bool:
    try:
        data = data.split('/')

        if len(data) != 3:
            raise ValueError('Formato inválido, lembre-se de inserir a data no formato dia/mês/ano. Ex: 05/12/2023')
            
        for i in range(len(data)):
            if not data[i].isdecimal():
                raise ValueError('Informe a data com números, não letras.')

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
        return ve
        
        

# Prepara a data para ser enviado na forma de comando do protocolo.
def comandoData(data:str) -> str:
    data = data.split('/')
    
    data[0] = int(data[0])
    data[1] = int(data[1])

    return f'{data[2]}-{str(data[1])}-{str(data[0])}'



# Recebe o comando do servidor, de mesas disponiveis, e o decodifica, de forma a deixá-lo legível ao cliente.
def decodificaMesas(indice:int, resposta:list):
    mesasDisponiveis = 'Mesas Disponíveis: '
    
    for i in range(indice, len(resposta)):
        mesasDisponiveis += resposta[i] + ' '

    mesasDisponiveis = mesasDisponiveis.removesuffix(' ') + '\n'
    return mesasDisponiveis



# Verifica se a mesa que o cliente escolheu é uma das opções que o servidor apresentou.
def validaMesa(mesaEscolhida:str, resposta:list, primeiraTentativa:bool) -> bool or str:
    if primeiraTentativa and mesaEscolhida in resposta[2:]:
        return False

    elif not primeiraTentativa and mesaEscolhida in resposta[3:]:
        return False

    else:
        return 'Informe uma mesa que se encontra na lista de mesas disponíveis.\n'
        
    

# Decodifica as reservas, deixando-as de forma legível para o cliente.
def decodificaReservas(resposta:list) -> str:

    reservas = '\n'
    for i in range(2, len(resposta)):
        dados = resposta[i].split(':')

        dia = dados[2]
        mes = dados[1]
        ano = dados[0]
        mesa = dados[3]

        reservas += f'Data: {dia}/{mes}/{ano} --> Mesa Reservada: {mesa}\n'

    return reservas



def validaReservaDeletar(reservaDeletar:str, resposta:list):
    reservaDeletar = reservaDeletar.split('/')

    try:
        
        dia = int(reservaDeletar[0])
        mes = int(reservaDeletar[1])
        ano = reservaDeletar[2]
        mesa = reservaDeletar[3]
    except Exception:
        return 'Favor digitar uma reserva válida. Lembre-se do formato dia/mês/ano/mesa\n'

    dia = str(dia)
    mes = str(mes)

    aux = f'{ano}:{mes}:{dia}:{mesa}'

    if aux in resposta:
        return False

    return 'Favor digitar uma reserva válida. Lembre-se do formato dia/mês/ano/mesa\n'



# Função para enviar o comando da requisição para o servidor. Devolve a resposta já decodificada e já feito o split.
def enviarParaServidor(comando):
    sock.sendto(comando.encode(), server_address)

    resposta, address = sock.recvfrom(1024)
    
    return resposta.decode().split('-')



hostIP = 'localhost'

if len(sys.argv) > 1:
    hostIP = sys.argv[1]

server_address = (hostIP, 60000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



option = ''
print('*****Gerenciador de Reservas GAIA*****') # GAIA = George Amanda IAn
time.sleep(2)


# Inserção do nome do cliente com verificações.
nomeValido = False
while not nomeValido:
    nomeCliente = input('Informe seu nome: ')
    nomeValido = validaNomeCliente(nomeCliente)

    if type(nomeValido) != bool:
        print(nomeValido)
        nomeValido = False
        time.sleep(3)


# Inserção do CPF do cliente com verificações.
cpfValido = False
while not cpfValido:
    cpfCliente = input('Informe seu cpf: ')
    cpfValido = validaCPF(cpfCliente)

    if type(cpfValido) != bool:
        print(cpfValido)
        cpfValido = False
        time.sleep(3)


print(f'\nBem-vindo {nomeCliente}, vamos começar?\n')
time.sleep(2)


# Menu de opções.
while option != 's':

    print(f'\n{"OPERAÇÕES":^30}')
    print(f'{"":=^30}')
    print('(n) --> Fazer uma nova reserva')
    print('(d) --> Excluir uma reserva efetuada')
    print('(l) --> Listar todas as reservas efetuadas.')
    print('(s) --> Encerrar sua conexão\n')

    option = input(f'{"DIGITE A OPÇÃO DESEJADA ":^30}\n\n{"":13}')


    # Nova reserva
    if option == 'n': 
        comando = f'CLI-NEW-<1>-{nomeCliente}:{cpfCliente}-'
        
        # Aqui pede para o cliente informar a data da reserva até que seja inserido uma data válida.
        dataValida = False
        while not dataValida:
            data = input('\nInforme a data na qual deseja realizar a reserva no formato dia/mês/ano: ')
            dataValida = validaData(data)

            if type(dataValida) != bool:
                print(dataValida)
                dataValida = False
                time.sleep(3)

        # Envia requisição ao servidor e recebe a resposta informando as mesas disponíveis daquele dia.
        comando += comandoData(data)
        resposta = enviarParaServidor(comando)
        
        status = resposta[0]

        # Tratamento de erro
        if status == '200':
            print('Infelizmente não há mais mesas disponíveis nesse dia.\n')
            time.sleep(3)
            continue
        

        # Primeira tentativa de efetuar reserva em uma mesa específica.
        primeiraTentativa = True
        desistiu = False
        while True:
            indice = 2

            # Caso não seja a primeira tentativa, é necessário retirar do comando a mesa anterior que o cliente tentou reservar mas falhou.
            # Também é necessário mudar o índice devido a resposta de erro do servidor ter um índice a mais do que a resposta informando que deu certo.
            if not primeiraTentativa:
                indice = 3
                comando = comando.removesuffix(f'-{mesaEscolhida}')

            # Decodifica o protocolo e apresenta ao cliente as mesas disponíveis para reserva daquele dia.        
            mesasDisponiveis = decodificaMesas(indice, resposta)
            print(mesasDisponiveis)


            # Aqui inicia o processo de pedir ao cliente que escolha uma mesa, e verificar se ela é válida.
            mesaInvalida = True
            while mesaInvalida:

                mesaEscolhida = input('Informe a mesa que deseja reservar: ')
                
                # Cliente pode digitar QUIT a qualquer momento para desistir da reserva.
                if mesaEscolhida.upper() == 'QUIT':
                    print('Reserva cancelada.\n')
                    desistiu = True
                    time.sleep(3)
                    break
                
                # Verifica se a mesa que o cliente informou se encontra na lista de mesas que o servidor devolveu.
                mesaInvalida = validaMesa(mesaEscolhida, resposta, primeiraTentativa)

                # Caso o cliente tenha escolhido uma mesa inválida, mesnagem de erro é imprimida na tela, e reinicia-se o processo. 
                if type(mesaInvalida) != bool:
                    print(mesaInvalida)
                    mesaInvalida = True
                    time.sleep(3)



            # Caso o cliente tenha desistido da reserva, encerra o algoritmo e volta para o menu de opções.
            if desistiu:
                desistiu = False
                break

            # Codifica o comando de acordo com o protocolo e o manda para o servidor.
            comando += f'-{mesaEscolhida}'
            comando = comando.replace('<1>', '<2>')
            resposta = enviarParaServidor(comando)

            status = resposta[0]


            # Caso tenha dado tudo certo.
            if status == '100':
                print('Reserva inserida com sucesso!\n')
                time.sleep(3)
                break

            # Caso o cliente tenha demorado demais e, quando o servidor foi tentar efetuar a reserva, já não havia mais mesas disponíveis
            # naquele dia.
            elif status == '200':
                print('Infelizmente não há mais reservas disponíveis para esse dia.\n')
                time.sleep(3)
                break

            # Caso o cliente tenha demorado demais e, quando o servidor foi tentar efetuar a reserva, outro cliente já havia reservado
            # a mesa, mas outras ainda estavam disponíveis, o servidor devolve uma mensagem de erro com uma nova lista de mesas disponiveis,
            # e é reiniciado o processo de escolha de mesa válida.
            
            # Como o padrão de mensagem do erro 201 é diferente do da mensagem de acerto, é necessário fazer algumas mudanças em como
            # o código irá tratar o protocolo, para isso informamos ao programa que houve essa mudança com o primeiraTentativa = False.
            elif status == '201':
                print('Infelizmente, outro cliente foi mais veloz, e efetou uma reserva nessa mesa enquanto você se decidia. Por favor escolha outra mesa para reservar. Você também pode digitar QUIT para cancelar a reserva.\n')
                time.sleep(7)
                primeiraTentativa = False

            elif status == '203':
                print('Você já possui outra reserva nesse dia. Caso deseje alterá-la, primeiro deverá deletá-la.\n')
                time.sleep(3)
                break
            


    # Listar reservas efetuadas pelo cliente.
    elif option == 'l' or 'd':

        # Prepara o comando e já envia a requisição da listagem para o servidor.
        comando = f'CLI-LIST-<1>-{nomeCliente}:{cpfCliente}'
        resposta = enviarParaServidor(comando)

        status = resposta[0]

        # Caso não haja reserva alguma do cliente no servidor.
        if status == '202':
            if option == 'l':
                print(f'\nNão há reserva sua no servidor, aguardamos ansiosamente pela primeira {nomeCliente}!\n')

            else:
                print('\nNão há reserva sua no servidor, logo não há o que deletar.\n')
                
            time.sleep(3)
            continue
        
        # Decodifica as reservas, e mostra para o lciente todas as reservas que efetuou até o momento.
        reservasEfetuadas = decodificaReservas(resposta)
        print('\n', reservasEfetuadas, '\n')

        if option == 'l':
            print('Essas são todas as suas reservas efetuadas até o momento.')
            input('Para voltar ao menu, digite ENTER.\n')

        else:
            reservaDeletarInvalida = True
            while reservaDeletarInvalida:
                reservaDeletar = input('Digite a data da reserva a qual deseja deletar, no formato dia/mês/ano/mesa: ')
                
                reservaDeletarInvalida = validaReservaDeletar(reservaDeletar, resposta)

                if type(reservaDeletarInvalida) != bool:
                    print(reservaDeletarInvalida)
                    reservaDeletarInvalida = True
                    time.sleep(3)

            comando = f'CLI-DEL-<1>-{nomeCliente}:{cpfCliente}-'
            comando += comandoData(reservaDeletar)

            resposta = enviarParaServidor(comando)

            status = resposta[0]

            if status == '100':
                print('Reserva removida com sucesso.\n')
                time.sleep(3)

    elif option == 's':
        print(f'Até a próxima {nomeCliente}!\n')
        