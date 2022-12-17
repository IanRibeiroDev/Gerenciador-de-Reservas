
serverStatus = {
    100: '+OK',
    400: '-ERR'
}

menu = {
    1: 'Envie 1 para: Fazer uma nova reserva',
    2: 'Envie 2 para: Alterar uma reserva efetuada',
    3: 'Envie 3 para: Excluir uma reserva efetuada',
    4: 'Envie 4 para: Listar todas as reservas efetuadas.', # Apenas no mês ou dia especificado, dependendo da complexidade da implementação.
    5: 'Envie 5 para: Encerrar sua conexão.'
} #Fazer isso aparecer para o cliente em linhas diferentes.

class ValidatingException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def validateMessage(message):
    messageDecode = message.decode().split(' ')
    try:
        if messageDecode[0] == 'Menu':
            return f'{serverStatus[100]} {menu[1], menu[2], menu[3], menu[4]}'
        
        elif messageDecode[0] == '1':
            return f'{serverStatus[100]} Procurando mesas disponíveis...' #Chamar método correspondente aqui.
            
        elif messageDecode[0] == '2':
            return f'{serverStatus[100]} Para fazer uma reserva envie a data desejada. Exemplo: 24/12/2022' #Chamar método correspondente aqui.
        
        elif messageDecode[0] == '3':
            return f'{serverStatus[100]} Para altera uma reserva informe seu identificador. Exemplo: 123456' #Acredito que a gente precisaria de algum identificador aqui. Usei isso só por enquanto mas podemos ver algo melhor.
            #Na verdade eu acho que a gente pode até deixar de lado essa funcionalidade se o tempo apertar.
        
        elif messageDecode[0] == '4':
            return f'{serverStatus[100]} Para excluir uma reserva informe seu identificador. Exemplo: 123456'

        elif messageDecode[0] == '5':
            return f'{serverStatus[100]} Conexão encerrada.'

        return f'{serverStatus[400]} Digite um comando válido.'
    except:
        raise ValidatingException (f'Erro interno. Verificando...')