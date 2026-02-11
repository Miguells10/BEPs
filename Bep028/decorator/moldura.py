from Bep028.decorator.display import DisplayDecorator


class MolduraDecorator(DisplayDecorator):
    def update(self, temperatura, umidade, pressao):
        print("╔══════════════════════════════╗")
        # Chama o display original (ex: DisplayGeral)
        self.display_decorado.update(temperatura, umidade, pressao)
        print("╚══════════════════════════════╝")