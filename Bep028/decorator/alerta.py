from Bep028.decorator.display import DisplayDecorator


class AlertaCriticoDecorator(DisplayDecorator):
    def update(self, temperatura, umidade, pressao):
        print("🚨 ALERTA: LEITURA CRÍTICA ABAIXO 🚨")
        self.display_decorado.update(temperatura, umidade, pressao)
        print("🚨 ---------------------------- 🚨")