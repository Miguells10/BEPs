import sqlite3

conn = sqlite3.connect("../faturaBD.db")

c = conn.cursor()

c.execute("PRAGMA foreign_keys = OFF;")

c.executescript('''
    CREATE TABLE ItensPedido(
    numFatura INTEGER PRIMARY KEY NOT NULL,
    codProduto_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    precoVenda REAL,
    FOREIGN KEY (codProduto_produto) REFERENCES Produto(codProduto)
    )''')

print("criou")

c.execute("DROP TABLE ItensFatura")
print("dropou")