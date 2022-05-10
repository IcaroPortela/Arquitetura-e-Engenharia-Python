import mysql.connector
from mysql.connector import Error, errorcode

class Agenda:
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password ='root',
        database = 'agenda'
    )

    cursor = db.cursor()

    def inserir(self):
        try:
            nomes = str(input("Informe o nome do contato: "))
            fone = str(input('Informe o telefone do contato: '))
            email = str(input("Informe o e-mail do contato: "))

            self.cursor.execute(f"insert into contatos(nomes, fones, email) Values('{nomes}','{fone}','{email}');")
            print('Dados cadastrados com sucesso!')
        except Error as erro:
            if erro.errno == errorcode.ER_BAD_DB_ERROR:
                print('Erro no banco de dados!')
            else:
                print('tudo ok!')
    
    def removerall(self):
        try:
            self.cursor.execute("delete from contatos;")
            print('Todos os contatos removidos com sucesso!')
        except Error as erro:
            if erro.errno == errorcode.ER_BAD_DB_ERROR:
                print('Erro no banco de dados!')
            else:
                print('tudo ok!')

    def removerone(self):
        try:
            name = str(input('Informe o nome que quer remover: '))
            self.cursor.execute(f"delete from contatos where nomes = '{name}';")
            print(f'Nome {name} removido com sucesso!')
        except Error as erro:
            if erro.errno == errorcode.ER_BAD_DB_ERROR:
                print('Erro no banco de dados!')
            else:
                print('tudo ok!')

    def alterar(self):
        try:
            while True:
                print('''
                    1.- Atualize o nome
                    2.- Atualize o email
                    3.- Atualize o telefone
                ''')
                
                opcao = int(input('Escolha uma das opções para atualizar: '))
                
                if opcao == 1:
                    name = str(input("Informe o nome que quer atualizar: "))
                    newname = str(input("Informe o novo nome: "))
                    self.cursor.execute(f"update contatos set nomes = '{newname}' where nomes = '{name}';")
                    print(f'Nome alterado com sucesso!')
                elif opcao == 2:
                    email = str(input("Informe o email que deseja alterar: "))
                    newmail = str(input('Informe o novo e-mail: '))
                    self.cursor.execute(f"update contatos set email = '{newmail} where email like '{email}';")
                    print('Email atualizado com sucesso!')
                elif opcao == 3:
                    fone = str(input("Informe o antigo número: "))
                    newfone = str(input('Informe o novo número: '))
                    self.cursor.execute(f"update contatos set fones = '{newfone}' where fones like '{fone}';")
                    print('Telefone atualizado com sucesso!')
                else:
                    print('Fim do processo, continue com no programa...')
                    break
        except Error as erro:
           if erro.errno == errorcode.ER_BAD_DB_ERROR:
                print('Erro no banco de dados!')
           else:
                print('tudo ok!')
    
    def pesquisaAll(self):
        try:
            self.cursor.execute("select * from contatos order by nomes;")
            agendas = self.cursor.fetchall()
            pos =0
            while pos < len(agendas):
                for i in range(len(agendas[pos])):
                    id = agendas[pos][0]
                    nome = agendas[pos][1]
                    fone = agendas[pos][2]
                    email = agendas[pos][3]
                    data = agendas[pos][4]
                print(f"""
                    ID: {id}
                    Nome: {nome}
                    Fone: {fone}
                    E-mail: {email}
                    Data: {data}
                    """)
                pos += 1
        except Error as erro:
           if erro.errno == errorcode.ER_BAD_DB_ERROR:
                print('Erro no banco de dados!')
           else:
                print('tudo ok!')

    def pesquisaOne(self):
        try:
            dados = str(input('Informe o nome que deseja pesquisar: '))
            self.cursor.execute(f"select nomes, fones, email from contatos where nomes like '{dados}'")
            agendas = self.cursor.fetchall()
            pos =0
            achar = False
            while achar == False and pos < len(agendas):
                for i in range(len(agendas[pos])):
                    if dados == agendas[pos][1]:
                        achar = True
                        id = agendas[pos][0]
                        nome = agendas[pos][1]
                        fone = agendas[pos][2]
                        email = agendas[pos][3]
                        data = agendas[pos][4]
                    else:
                        achar = False
                if achar == True:
                    print(f"Esses são os dados que você procurava: ")
                    print(f'''
                    ID: {id}
                    Nome: {nome}
                    Telefone: {fone}
                    E-mail: {email}
                    Data: {data}
                    ''')
                else:
                    print('Nome não foi encontrado!')
                pos += 1
        except Error as erro:
           if erro.errno == errorcode.ER_BAD_DB_ERROR:
                print('Erro no banco de dados!')
           else:
                print('tudo ok!')