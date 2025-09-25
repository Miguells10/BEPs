import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mi1234",
    database="mydb"
)

c = conn.cursor()

compradores = [
    ("12345678900", "Miguel", "Solteiro", None, None),
    ("98765432100", "Ana", "Casado", "Carlos", "11122233344")
]
c.executemany("""
    INSERT IGNORE INTO comprador (cpf, nome, estadoCivil, nomeConjuge, cpfConjuge)
    VALUES (%s, %s, %s, %s, %s)
""", compradores)

corretores = [
    (101, "Prof. Ana", "2020-01-15"),
    (102, "Prof. Bruno", "2019-06-10")
]
c.executemany("""
    INSERT IGNORE INTO corretor (nrMatricula, nome, dataAdmissao)
    VALUES (%s, %s, %s)
""", corretores)

vendas = [
    (1, "2025-09-01", 50000.0, 2500.0, "12345678900", 101),
    (2, "2025-09-05", 75000.0, 3750.0, "98765432100", 102)
]
c.executemany("""
    INSERT IGNORE INTO venda (idvenda, dataVenda, valorVenda, comissao, comprador_cpf, corretor_nrMatricula)
    VALUES (%s, %s, %s, %s, %s, %s)
""", vendas)

marcas = [
    (1, "Fiat"),
    (2, "Volkswagen")
]
c.executemany("""
    INSERT IGNORE INTO Marca (idMarca, nome)
    VALUES (%s, %s)
""", marcas)

modelos = [
    (1, "Palio", 1),
    (2, "Golf", 2)
]
c.executemany("""
    INSERT IGNORE INTO modelo (idmodelo, nome, Marca_idMarca)
    VALUES (%s, %s, %s)
""", modelos)

veiculos = [
    (1, "CHS12345", "2023-01-01", "Vermelho", 10000, 1, 1),
    (2, "CHS67890", "2022-05-15", "Azul", 20000, 2, 2)
]
c.executemany("""
    INSERT IGNORE INTO veiculo (idVeiculo, chassi, anoFabricacao, cor, quilometragem, venda_idvenda, modelo_idmodelo)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", veiculos)

conn.commit()

c.execute("SELECT * FROM comprador")
print("Compradores:", c.fetchall())

c.execute("SELECT * FROM corretor")
print("Corretores:", c.fetchall())

c.execute("SELECT * FROM venda")
print("Vendas:", c.fetchall())

c.execute("SELECT * FROM Marca")
print("Marcas:", c.fetchall())

c.execute("SELECT * FROM modelo")
print("Modelos:", c.fetchall())

c.execute("SELECT * FROM veiculo")
print("Veículos:", c.fetchall())

c.close()
conn.close()
