from Bep19.tratamento import PrecoInvalidError

class Ingresso:
    _contador_codigo = 0

    def __init__(self, preco):
        if preco <= 0:
            raise PrecoInvalidError("O preço deve ser maior que 0 (zero).")

        Ingresso._contador_codigo += 1
        self.codigo = Ingresso._contador_codigo
        self.preco = preco
        self.status = "Disponível"

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise PrecoInvalidError("O preço deve ser maior que 0 (zero).")
        self._preco = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        self._status = valor

    def vender(self):
        self.status = "Vendido"

    def __str__(self):
        return f"Código: {self.codigo}, Preço: R$ {self.preco:.2f}, Status: {self.status}"
