import sqlite3
from sqlite3.dbapi2 import Cursor

def Conexao():
    try:
        db = sqlite3.connect('Estoque.db')
        Cursor.cursor = db.cursor()
        print("Conectado!")
    except:
        print("Falha de conexão com o Banco de dados!")

Conexao()
