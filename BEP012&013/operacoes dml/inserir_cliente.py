import sqlite3

conn = sqlite3.connect("../faturaBD.db")

c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON;")

clientes = [
    ("0001", "Miguel", "Rua A", "Vip", "089.192.495-08", "Paga muito"),
    ("0002", "Lucas", "Rua B", "Prata", "090.192.495-08", "Paga muito"),
    ("0003", "Santana", "Cidade A", "Ouro", "189.192.495-08", "Paga muito"),
    ("0004", "Freire", "Cidade A", "Ouro", "139.192.495-08", "Paga muito"),
    ("0005", "Jose", "Cidade A", "Ouro", "189.492.495-08", "Paga muito"),
    ("0006", "Frederico", "Cidade A", "Ouro", "189.492.495-08", "")
]

c.executemany("INSERT OR IGNORE INTO Cliente VALUES (?,?,?,?,?,?)", clientes)

conn.commit()

# b)
c.executescript("UPDATE Cliente SET endereco = 'Rua das Palmeiras, 123' WHERE codCliente = '0001'")

# c)
c.executescript("UPDATE Cliente SET tipo = 'Premium' WHERE endereco = 'Cidade A'")

# d) remover cliente 003
c.execute("DELETE FROM Cliente WHERE codCliente = '0003'")

# e) Remover clientes com historico NULL ou vazio
c.execute("DELETE FROM Cliente WHERE historico IS NULL OR historico = ''")

conn.commit()
conn.close()