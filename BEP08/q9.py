'''Crie uma função criar_perfil_usuario que aceite dois argumentos obrigatórios
(nome e email) e uma quantidade variável de informações adicionais usando
argumentos nomeados (**kwargs). A função deve montar e retornar um
dicionário contendo todas as informações do perfil do usuário'''


def criar_perfil_usuario (nome, email, **kwargs):
    perfil = {"Nome: ": nome,
              "Email: ":email}
    perfil.update(kwargs)

    return perfil

print(criar_perfil_usuario("Miguel", "dasdasdasdad.com", idade=21, tamanho=1.8))

