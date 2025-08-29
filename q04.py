'''4. Você recebeu uma lista de e-mails de participantes de um evento, mas a lista contém
vários e-mails duplicados. Sua tarefa é criar uma nova coleção que contenha apenas os
e-mails únicos e, em seguida, imprimir a quantidade de participantes únicos.
Dados de Entrada:'''

emails_participantes = ['ana@email.com', 'bruno@email.com', 'carla@email.com',
'daniel@email.com' ,'ana@email.com' ,'bruno@email.com', 'emilia@email.com']

emails_unicos = set(emails_participantes)
quantidade_unicos = len(emails_unicos)
print(f'Quantidade de participantes únicos: {quantidade_unicos}')
print('E-mails únicos:')
for email in emails_unicos:
    print(email)
