import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED, Cancel, Window

sg.theme("Dark Blue 3")

#Layout
layout = [
    [sg.Text('Login'),sg.Input(key='login', size=(10,0))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(10,0))],
    [sg.Button('Entrar'),sg.Button('Cadastre-se', auto_size_button='')]
]
layout2 = [
    [sg.Canvas(size=(200,100))],
    [sg.Button('CADASTRO'), sg.Button('CONTROLE DE ALMOXARIFADO'), sg.Button('CONTROLE DE ESTOQUE')],
    [sg.Button('ENTRADA'),sg.Button('SAÍDA')]
]
#Janela
janela = sg.Window('Tela de Acesso', layout)
janela2 = sg.Window('Controle de Estoque', layout2)

#Evento
while True:
    event, values = janela.read()
    evento = janela2.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Entrar':
        if values['login'] == 'icaro' and values['senha'] == '123456':
            print('Bem Vindo!')
    if evento == WIN_CLOSED:
        break
Window.close()
