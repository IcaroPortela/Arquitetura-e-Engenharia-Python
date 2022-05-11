from controller import *

def menu():
    gmail = Gmail()
    outlook = Outlook()
    tela = """
    1 - Enviar pelo outlook
    2 - Enviar pelo gmail
    3 - Finalizar app
    """
    while True:
        print('~' * 50)
        print(tela)
        op = int(input('Escolha a opção: '))
        print('~' * 50)
        
        if op == 1:
            outlook.send_outlook()
        elif op == 2:
            gmail.send_gmail()
        elif op == 3:
            print('Finalizando o programa...')
            break
        else:
            print('Digite a opção correta!')

menu()