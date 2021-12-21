from bottle import route

def meu_decorator(imprime):
    def imprime2():
        print('não sei somar')
    return imprime2

@meu_decorator
def imprime():
    print('Eu sei somar')

imprime()

class Mensagem():
    def __init__(self,name):
        self.name = name
    #msg= 'Olá mundo!'
    def funcao(self):
        print("Olá meu nome é", self.name)

m1 = Mensagem('Ana')
m1.funcao()