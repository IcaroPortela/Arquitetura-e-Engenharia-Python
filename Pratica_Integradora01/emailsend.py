"""
import win32com.client as win32
msg = "Olá Mundo!"

#Cria uma integração com o outlook
outlook = win32.Dispatch('outlook.application')

#Criar um e-mail
email = outlook.CreateItem(0)

#Configurar as informações do e-mail
email.To = "Destinatário"

email.Subject = "Assunto do e-mail"

#email.Body = """""" # Este comando caiu em desuso

email.HTMLBody = f'''
    <p>Msg em html</p>
    <p>{msg}</p>
'''
#Anexa um arquivo no e-mail
anexo = "C://Users/icaro.portela/Documents/Python/agendaPy/menu.py"
email.Attachments.Add(anexo)

#Envia o email
email.Send()

#Menssagem final do código
print('E-mail enviado com sucesso!')

"""


from pydantic import EmailError
import win32com.client as win32

def autoEmail():
    try:
        outlook = win32.Dispatch('outlook.application')
        email = outlook.CreateItem(0)
        
        destinatario = input('Informe o email de destino: ')
        assunto = input('Informe o assunto que se trata o e-mail: ')
        
        email.To = destinatario
        email.Subject = assunto
        email.HTMLBody = f"""
        <h1> Parabéns você foi cadastrado com sucesso!</h1>
        <p>Este é um e-mail automático por favor não responder</p>
        <p>Abs,</p>
        <b>Equipe SysOps</b>
        """

        anex = input('Desenja anexar algum arquivo: S/N: ')
        if anex == anex.lower():
            anexo = input('Informe o caminho do arquivo: ')
            email.Attechments.Add(anexo)
        else:
            print('Não será enviado nenhum arquivo. ')
        
        email.Send()
        print('E-mail enviado com sucesso!')
    except EmailError as erro:
        print(erro)

autoEmail()