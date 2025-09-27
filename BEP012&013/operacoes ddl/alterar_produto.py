import sqlite3

conn = sqlite3.connect("../faturaBD.db")

c = conn.cursor()

c.execute("PRAGMA foreign_keys = OFF;")

c.executescript('''
    CREATE TABLE Produto_novo(
    codProduto INTEGER PRIMARY KEY NOT NULL,
    descricao VARCHAR(25),
    precoCompra REAL)''')

c.executescript('''DROP TABLE Produto''')

c.executescript('''ALTER TABLE Produto_novo RENAME TO Produto''')

c.execute("PRAGMA foreign_keys = ON;")

conn.commit()
conn.close()