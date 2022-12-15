
def validateMessage(message):
    messageDecode = message.decode().split(',')

    if messageDecode[0] == 'RSV':
        return 'Deseja reservar. Processando...'
    
    elif messageDecode[0] == 'ALT':
        return 'Deseja alterar. Processando...'
        
    elif messageDecode[0] == 'DEL':
        return 'Deseja excluir. Processando...'
    
    elif messageDecode[0] == 'FIM':
        return 'Conexão encerrada.'
    
    return 'Digite um comando válido.'