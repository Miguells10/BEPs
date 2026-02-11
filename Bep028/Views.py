from Bep028.Observadores import Observadores


class DisplayTemperatura(Observadores):
    def update(self, temperatura, umidade, pressao):
        print(f"🌡️  Display Temperatura: {temperatura}°C")

class DisplayUmidade(Observadores):
    def update(self, temperatura, umidade, pressao):
        print(f"💧 Display Umidade: {umidade}%")

class DisplayPressao(Observadores):
    def update(self, temperatura, umidade, pressao):
        print(f"🏋️  Display Pressão: {pressao} hPa")

class DisplayGeral(Observadores):
    """Um display que mostra tudo junto."""
    def update(self, temperatura, umidade, pressao):
        print(f"📊 Display Geral: {temperatura}°C | {umidade}% | {pressao}hPa")