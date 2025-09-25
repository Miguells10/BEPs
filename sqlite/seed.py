import sqlite3

conn = sqlite3.connect('concessionaria.db')
c = conn.cursor()

c.execute("PRAGMA foreign_keys = ON;")

compradores = [
    ("12345678900", "Miguel", "Solteiro", None, None),
    ("98765432100", "Ana", "Casado", "Carlos", "11122233344")
]
c.executemany("INSERT OR IGNORE INTO comprador VALUES (?,?,?,?,?)", compradores)

corretores = [
    (101, "Corretora Ana", "2020-01-15"),
    (102, "Corretor Bruno", "2019-06-10")
]
c.executemany("INSERT OR IGNORE INTO corretor VALUES (?,?,?)", corretores)

vendas = [
    (1, "2025-09-01", 50000.0, 2500.0, "12345678900", 101),
    (2, "2025-09-05", 75000.0, 3750.0, "98765432100", 102)
]
c.executemany("INSERT OR IGNORE INTO venda VALUES (?,?,?,?,?,?)", vendas)

marcas = [
    (1, "Fiat"),
    (2, "Volkswagen"),
    (3, "Ford")
]
c.executemany("INSERT OR IGNORE INTO Marca VALUES (?,?)", marcas)

modelos = [
    (1, "Palio", 1),
    (2, "Golf", 2),
]
c.executemany("INSERT OR IGNORE INTO modelo VALUES (?,?,?)", modelos)

veiculos = [
    (1, "CHS12345", "2023-01-01", "Vermelho", 10000, 1, 1),
    (2, "CHS67890", "2022-05-15", "Azul", 20000, 2, 2),
]
c.executemany("INSERT OR IGNORE INTO veiculo VALUES (?,?,?,?,?,?,?)", veiculos)

conn.commit()

print("foi")

conn.close()
