import sqlite3

conn = sqlite3.connect('concessionaria.db')
c = conn.cursor()

'''Atualizar estado civil'''

up = c.execute(
    "UPDATE COMPRADOR SET estadoCivil = 'Solteiro' WHERE cpf = '98765432100'"
)

consulta = c.execute("Select * from COMPRADOR")

'''Atualizar comissao'''

comissao = c.execute("UPDATE venda SET valorVenda = 194949 WHERE idvenda = 1")

for i in comissao:
    print(i)
'''Remover dados de cliente'''

try:
    conn.execute("DELETE FROM comprador WHERE cpf = '98765432100'")

    consultar = c.execute("SELECT * FROM comprador")

    for i in consultar:
        print(i)
except sqlite3.IntegrityError as e:
    print(e)
    conn.rollback()
finally:
    conn.commit()
