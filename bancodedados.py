import sqlite3
conexao = sqlite3.connect("escolinha.db")
comanddoo = conexao.cursor()
while True:
    try:
      dados = (input("digite o nome:  "), int(input("digite a idade:  ")), input("digite o email:  "), input("digite a data de nascimento (AAAA-MM-DD):  "), input("digite o CPF:  "))
      break
    except ValueError:
      print("digite  um valor valido em idade ")
comanddoo.execute("""CREATE TABLE IF NOT EXISTS alunos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome  TEXT NOT NULL,
idade  INTEGER NOT NULL,
email TEXT NOT NULL,
data_de_nacimento DATE NOT NULL,
CPF TEXT NOT NULL
)""")
comanddoo.execute(""" INSERT INTO alunos (nome,idade,email,data_de_nacimento,CPF) VALUES (?,?,?,?,?)""",(dados))
conexao.commit()
conexao.close()