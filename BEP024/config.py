class Configuracoes:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Configuracoes, cls).__new__(cls, *args, **kwargs)
            cls._instance.empresa = "Empresa Padrão"

        return cls._instance

    def get_config(self) -> str:
        return f"Configurações da empresa: {self.empresa}"