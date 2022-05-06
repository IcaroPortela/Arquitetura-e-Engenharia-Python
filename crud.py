import mysql.connector

mysql = mysql.connector.connect(host='localhost', user='root', password='root', database='RHdescomplica01')
cur = mysql.cursor()

#Comandos DDL, DCL, DML

#Comandos
#Select
def select(colluns, tables, options):
    cur.execute(f'Select {colluns} from {tables} {options}')

    teste = cur.fetchall()

    for exemplo in teste:
        print(exemplo)

#Comandos DML
#Insert, Delete, Update
def insert(table, colunas, valores):
    cur.execute(f'Insert into {table}({colunas}) values({valores})')
    return print('Dados inseridos com sucesso!')

def delete(table,column,value):
    cur.execute(f'Delete * from {table} where {column} = "{value}"')

def update(table, data, column):
    cur.execute(f'Update {table} ')

#Comandos DDL
#Create, Alter Drop
def CreateDatabase(Database):
    cur.execute(f'Create database {Database}')
    print(f'{Database} criado com sucesso!')

def CreateTable(table,coluns):
    cur.execute(f'''Create {table} ('{coluns}')''')

def Drop():
    opcoes = '''
        1.- Apagar o Banco de dados
        2.- Apagar uma tabela
        3.- Sair
    '''
    while(True):
        print(opcoes)
        op = int(input('Informe um número: '))
        if op == 1:
            database = str(input('Informe o nome do Banco de dados: '))
            cur.execute(f'Drop database {database}')
            print('banco de dados removido com suceso!')
        elif op == 2:
            table = str(input('Informe a tabela que deseja deletar: '))
            cur.execute(f'Drop table {table}')
            print('Tabela removida com sucesso!')
        else:
            break

def AlterTable(table, column):
    cur.execute(f'Alter {table} {column}')
