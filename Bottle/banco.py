import sqlite3
try:
    print('criando arquivo')
    open('meubanco.db', 'wt+')
    print('arquivo criado com sucesso, executando conexão...')
    con = sqlite3.connect('meubanco.db')
    con.commit()
    print('Sucesso! Contectado com o banco!')
except Exception:
    print("Erro não foi possível conectar")

try:
    con = sqlite3.connect('meubanco.db')
    con.commit()
    print('Sucesso! Contectado com o banco!')

    cur = con.cursor()
    print('Criando o banco...')

    cur.execute("Create database meubanco")
    print('Banco criado com sucesso, criando tabela')

    cur.execute("Create table tabeladb(id int primary key auto_incrementh, nome varchar(20), login varchar(20));")
    print('Tabela criada com sucesso!')
    
    cur.execute("Insert into tabeladb Values('José','1234ze')")
    meuBanco = cur.execute("Select * from tabeladb")
    print(meuBanco)
except Exception:
    print("Erro não foi possível criar,nem inserir os dados e nem impirmir os dados! Tente novamente!")