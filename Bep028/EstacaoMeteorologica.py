from Bep028.Sujeito import Sujeito


class EstacaoMeteorologica(Sujeito):
    def __init__(self):
        super().__init__()
        self._temperatura = 0.0
        self._pressao = 0.0
        self.umidade = 0.0

    def set_medidas(self, temperatura, umidade, pressao):
        print(f"\n--- Novos dados recebidos na Estação ---")
        self._temperatura = temperatura
        self._umidade = umidade
        self._pressao = pressao
        self.notificar_observadores(self._temperatura, self._umidade, self._pressao)