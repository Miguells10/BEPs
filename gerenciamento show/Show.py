class Show:
    def __init__(self, nome, data, local):
        self.nome = nome
        self.data = data
        self.local = local
        self.lista_ingressos = []

    def adicionar_ingresso(self, ingresso):
        self.lista_ingressos.append(ingresso)

    def listar_ingressos_disponiveis(self):
        print(f"\nIngressos disponíveis para {self.nome}:")
        for i in self.lista_ingressos:
            if i.status == "Disponível":
                print(i)

    def listar_ingressos_vendidos(self):
        print(f"\nIngressos vendidos para {self.nome}:")
        for i in self.lista_ingressos:
            if i.status == "Vendido":
                print(i)

    def calcular_total_arrecadado(self):
        total = 0
        for i in self.lista_ingressos:
            if i.status == "Vendido":
                total += i.preco
        return total

    def __str__(self):
        return (
            f"Show: {self.nome}, Data: {self.data}, Local: {self.local}, "
            f"Total de ingressos: {len(self.lista_ingressos)}"
        )
