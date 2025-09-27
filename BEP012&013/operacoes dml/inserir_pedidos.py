import sqlite3
from datetime import date

conn = sqlite3.connect("../faturaBD.db")
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON;")

# a) INSERT: criar pelo menos 3 novos pedidos
pedidos = [
    (1, "0001", "2023-05-10"),
    (2, "0002", "2024-02-15"),
    (3, "0004", "2022-12-30")
]

c.executemany("INSERT OR IGNORE INTO Pedidos VALUES (?,?,?)", pedidos)

# b) UPDATE: alterar a data do pedido com idFatura = 1 para a data atual
c.execute("UPDATE Pedidos SET dataPed = ? WHERE idFatura = 1", (date.today().isoformat(),))

# c) DELETE: remover pedidos feitos antes de 2023-01-01
c.execute("DELETE FROM Pedidos WHERE dataPed < '2023-01-01'")

conn.commit()
conn.close()
