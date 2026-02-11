from Bep028.EstacaoMeteorologica import EstacaoMeteorologica
from Bep028.Views import DisplayTemperatura, DisplayUmidade, DisplayPressao, DisplayGeral
from Bep028.controller.clima import ControladorClima
from Bep028.decorator.alerta import AlertaCriticoDecorator
from Bep028.decorator.moldura import MolduraDecorator

if __name__ == "__main__":
    estacao = EstacaoMeteorologica()

    controlador = ControladorClima(estacao)

    display_temp = DisplayTemperatura()
    display_umid = DisplayUmidade()

    display_geral_bonito = MolduraDecorator(DisplayGeral())

    display_pressao_alerta = AlertaCriticoDecorator(DisplayPressao())

    print("--> Registrando observadores...")
    estacao.registrar_observadores(display_temp)
    estacao.registrar_observadores(display_umid)
    estacao.registrar_observadores(display_geral_bonito)
    estacao.registrar_observadores(display_pressao_alerta)

    controlador.atualizar_dados_sensor(25, 60, 1013)
    controlador.atualizar_dados_sensor(28, 55, 1010)