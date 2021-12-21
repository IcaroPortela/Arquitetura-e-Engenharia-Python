import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [  [sg.Text('Envie um formulário')],
            [sg.Text('Digite seu nome'), sg.InputText()],
            [sg.Button('Enviar'), sg.Button('Sair')] ]


window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values[0])

window.close()