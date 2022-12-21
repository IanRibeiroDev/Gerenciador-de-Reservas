class NodeLista:
    def __init__(self, carga:any):
        self.carga = carga
        self.prox = None
        

class NodeArvore(): 
    '''Class used to create a generic tree node instance in memory'''
    def __init__(self, value): 
        self.value = value 
        self.left = None
        self.right = None
        self.height = 1 # atributo que especifica a altura que determina o fator de balanco do nó
    
    def __str__(self):
        return f'|{self.value}:h={self.height}|'
