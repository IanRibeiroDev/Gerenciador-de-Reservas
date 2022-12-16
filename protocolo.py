
serverStatus = {
    100: '+OK',
    400: '-ERR'
}

def validatingException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def validateMessage(message):
    messageDecode = message.decode().split(' ')
    try:
        if messageDecode[0] == 'RSV':
            return f'{serverStatus[100]} Deseja reservar. Processando...'
        
        elif messageDecode[0] == 'ALT':
            return f'{serverStatus[100]} Deseja alterar. Processando...'
            
        elif messageDecode[0] == 'DEL':
            return f'{serverStatus[100]} Deseja excluir. Processando...'
        
        elif messageDecode[0] == 'FIM':
            return f'{serverStatus[100]} Conexão encerrada.'
        
        return f'{serverStatus[400]} Digite um comando válido.'
    except:
        raise validatingException (f'Erro interno. Verificando...')