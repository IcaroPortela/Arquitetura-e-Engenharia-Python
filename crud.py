import mysql.connector

mysql = mysql.connector.connect(host='localhost', user='root', password='root', database='RHdescomplica01')
cur = mysql.cursor()

def select(colluns, tables, options):
    cur.execute(f'Select {colluns} from {tables} {options}')

    teste = cur.fetchall()

    for exemplo in teste:
        print(exemplo[4])

def insert(table, colunas, valores):
    cur.execute(f'Insert into {table}({colunas}) values({valores})')
    return print('Dados inseridos com sucesso!')

def delete():
    cur.execute('')