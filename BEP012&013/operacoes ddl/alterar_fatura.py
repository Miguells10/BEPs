import sqlite3

conn = sqlite3.connect("../faturaBD.db")

c = conn.cursor()

c.execute("ALTER TABLE Fatura RENAME TO Pedidos;")

c.execute("ALTER TABLE Pedidos ADD COLUMN dataPed DATE;")

conn.commit()
conn.close()