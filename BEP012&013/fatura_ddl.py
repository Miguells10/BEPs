import sqlite3

conn = sqlite3.connect('faturaBD.db')
c = conn.cursor()

c.execute("PRAGMA foreign_keys = ON;")

c.executescript('''
    CREATE TABLE IF NOT EXISTS Cliente (
     codCliente INTEGER PRIMARY KEY NOT NULL,
     nomeCliente VARCHAR(45) NOT NULL,
     endereco VARCHAR(45) NOT NULL,
     credito DOUBLE NOT NULL, 
     tipo VARCHAR(20), 
     CPF VARCHAR(8))''')

c.executescript('''
    CREATE TABLE IF NOT EXISTS Produto(
    codProduto INTEGER PRIMARY KEY NOT NULL,
    descricao VARCHAR(45))''')

c.executescript('''
    CREATE TABLE IF NOT EXISTS Fatura (
    idFatura INTEGER PRIMARY KEY NOT NULL,
    codCliente_cliente INTEGER NOT NULL,
    FOREIGN KEY (codCliente_cliente) REFERENCES Cliente(codCliente)) ''')


c.executescript('''
    CREATE TABLE IF NOT EXISTS ItensFatura(
    numFatura INTEGER PRIMARY KEY NOT NULL,
    codProduto_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    valor DOUBLE NOT NULL,
    FOREIGN KEY (codProduto_produto) REFERENCES Produto(codProduto)
    )''')

c.close()