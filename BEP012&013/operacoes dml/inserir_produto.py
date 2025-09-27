import sqlite3

conn = sqlite3.connect("../faturaBD.db")
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON;")

# a) INSERT – 5 produtos
produtos = [
    ("P001", "Mouse Gamer", 120.00),
    ("P002", "Teclado Mecânico", 250.00),
    ("P003", "Monitor 24 Eletrônico", 900.00),
    ("P004", "Cabo HDMI", 35.00),
    ("P005", "Headset Eletrônico", 180.00),
]

c.executemany("INSERT OR IGNORE INTO Produto VALUES (?,?,?)", produtos)

conn.commit()

# b) UPDATE – aumenta preço em 10% para produtos que contenham "Eletrônico"
c.execute("""
    UPDATE Produto
    SET precoCompra = precoCompra * 1.10
    WHERE descricao LIKE '%Eletrônico%'
""")

# c) UPDATE – altera descrição do produto P002
c.execute("""
    UPDATE Produto
    SET descricao = 'Teclado Mecânico RGB'
    WHERE codProduto = 'P002'
""")

# d) DELETE – exclui produto com codProduto 'P005'
c.execute("DELETE FROM Produto WHERE codProduto = 'P005'")

# e) DELETE – remove produtos com precoCompra < 50.00
c.execute("DELETE FROM Produto WHERE precoCompra < 50.00")

conn.commit()
conn.close()
