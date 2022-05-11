import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import win32com.client as win32

class Gmail:
    def send_gmail(self):
        try:
            subject = "E-mail de Teste - PI2"
            sender_email = str(input("Informe o seu e-mail: "))
            receiver_email = str(input("Informe o(s) e-mail(s) para enviar: "))
            password = input("Informe a Senha:")
            body = str(input("Informe a menssagem que deseja enviar: "))

            # Cria uma messagem de multiplas partes e prepara o cabeçalho do e-mail
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email  # Recomendado para e-mails em massa

            # Addiciona ao corpo do e-mail
            message.attach(MIMEText(body, "plain"))

            anexar = str(input('Deseja enviar algum arquivo? '))
            if anexar == "s":
                filename = str(input("Informe o nome do arquivo: ")) # O arquivo deve estar no mesmo diretório do script
                # Abre o arquivo de PDF em modo binário
                with open(filename, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                print('arquivo anexado com sucesso!')
            else:
                print('não será enviado nenhum arquivo. ')
                # Addiciona um arquivo como application/octet-stream
                # Usualmente o cliente poderá baixa os arquivos de forma altoárica como attachment

            # Encode file in ASCII characters to send by email
            # Codifica o arquivo em ASCII para o envio do e-mail   
            encoders.encode_base64(part)

            # Addiciona o cabeçalho como uma chave/valor em pares para o Attachment
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # Adiciona o método attachment a messagem e e converte a messagem em string
            message.attach(part)
            text = message.as_string()

            # Logando ao servidor usando o contexto seguro e enviando o e-mail
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)

        except smtplib.SMTPException as erro:
            print(erro)
        except UnboundLocalError as localarquiv:
            print(localarquiv)
        finally:
            print('Finalizado o envio!')

class Outlook:
    def send_outlook(self):
        try:
            # Acesso ao app outlook na maquina
            # Cria um acesso e pergunta o login e senha ao usuário
            outlook = win32.Dispatch('outlook.application')
            email = outlook.CreateItem(0)
            
            #Armazena o destinatário e o assunto
            destinatario = input('Informe o email de destino: ')
            assunto = input('Informe o assunto que se trata o e-mail')
            body = input("Digite aqui a menssagem para o destinatário: ")
            
            #Armazena nas variaveis TO, Subject e HTMLBody os assuntos do e-mail
            email.To = destinatario
            email.Subject = assunto
            email.HTMLBody = body

            # Cria um arquivo em anexo
            anex = input('Desenja anexar algum arquivo: S/N: ')
            if anex == anex.lower():
                anexo = input('Informe o caminho do arquivo: ')
                email.Attechments.Add(anexo)
                print('Arquivo anexado com sucesso!')
            else:
                print('Não será enviado nenhum arquivo. ')
            
            email.Send()
            print('E-mail enviado com sucesso!')
        except smtplib.SMTPException as erro:
            print(erro)
        finally:
            print("E-mail finalizado!")