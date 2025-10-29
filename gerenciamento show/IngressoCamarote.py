from Bep19.Ingresso import Ingresso


class IngressoCamarote(Ingresso):
    def __init__(self, preco, localizacao):
        super().__init__(preco)
        self.localizacao = localizacao

    def __str__(self):
        return (f"Código: {self.codigo}, Preço: R$ {self.preco:.2f}, "
                f"Status: {self.status}, Localização: {self.localizacao}")