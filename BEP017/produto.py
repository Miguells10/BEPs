from BEP03.Q03 import quantidade


class Produto:
    contador_codigo = 1

    def __init__(self, nome = None, preco = 0, quantidade = 0):
        if nome == None:
            print("Produto criado")
        self.codigo = self.gerar_codigo()
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    @classmethod
    def gerar_codigo(self):
        contador = self.contador_codigo
        self.contador_codigo += 1
        return (contador)

    def calculcar_valor_estoque(self):
        total = self.preco * self.quantidade
        return print(f"Valor total do estoque do {self.nome}: {total}")

    def exibir_informacoes(self):
        print(f"""Codigo: {self.codigo}, Nome: {self.nome}, Preço: {self.preco}, Quantidade: {self.quantidade} """)

    def adicionar_quantidade(self):
        if quantidade > 0:
            self.quantidade = self.quantidade + 1
        else:
            print("A quantidade deve ser positiva")

    def remover_quantidade(self):
        if self.quantidade < 0:
            print("A quantidade para remover tem q ser maior q zero")
        else:
            self.quantidade = self.quantidade - 1

class Main:
    produto1 = Produto("Xbox", 1000, 30)
    produto1.exibir_informacoes()
    produto1.calculcar_valor_estoque()

    print()
    produto2 = Produto("Sabao")
    produto2.adicionar_quantidade()
    produto2.exibir_informacoes()
