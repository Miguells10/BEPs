from Bep028.EstacaoMeteorologica import EstacaoMeteorologica


class ControladorClima:
    def __init__(self, model: EstacaoMeteorologica):
        self.model = model

    def atualizar_dados_sensor(self, t, u, p):
        self.model.set_medidas(t, u, p)