import sqlite3

conn = sqlite3.connect("../faturaBD.db")

c = conn.cursor()

c.execute("PRAGMA foreign_keys = OFF;")

c.execute('''
    CREATE TABLE Cliente_novo (
        codCliente INTEGER PRIMARY KEY NOT NULL,
        nomeCliente VARCHAR(30) NOT NULL,
        endereco VARCHAR(45) NOT NULL,
        tipo VARCHAR(20),
        CPF VARCHAR(8),
        historico TEXT)''')

c.executescript("DROP TABLE Cliente;")

c.executescript("ALTER TABLE Cliente_novo RENAME TO Cliente;")

c.execute("PRAGMA foreign_keys = ON;")

conn.commit()
conn.close()