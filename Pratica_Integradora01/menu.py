from agenda import *

dados = Agenda()

while True:
    print("$" * 50)    
    print('''

        1.- Cadastrar contato
        2.- Remover contato
        3.- Apagar todos os contatos
        4.- Editar contato
        5.- Pesquisar contato (todos)
        6.- Pesquisar apenas um contato
        7.- Sair
    ''')
    op = int(input('Escolha uma opção: '))
    print("$" * 50) 
    
    if op == 1:
        dados.inserir()
    elif op == 2:
        dados.removerone()
    elif op == 3:
        dados.removerall()
    elif op == 4:
        dados.alterar()
    elif op == 5:
        dados.pesquisaAll()
    elif op == 6:
        dados.pesquisaOne()
    else:
        print('\nFinalizando o programa...')
        break