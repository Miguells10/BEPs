from Bep19.ControleShow import ControleShow
from Bep19.Show import Show


class Main:
    def __init__(self):
        self.controle_show = ControleShow()

    def escolher_opcao(self, escolha):
        match escolha:
            case "1":
                nome = input("Nome do show: ")
                data = input("Data do show (DD/MM/AAAA): ")
                local = input("Local do show: ")
                self.controle_show.cadastrar_show(nome, data, local)
                print(f"Show {nome} cadastrado com sucesso.")
            case "2":
                show_nome = input("Nome do show: ")
                tipo = input("Tipo de ingresso (pista/camarote): ")
                quantidade = int(input("Quantidade de ingressos: "))
                preco = float(input("Preço do ingresso: "))
                localizacao = input("Localização (apenas para camarote, deixe vazio para pista): ")
                if tipo == "camarote":
                    localizacao = input("Localização do camarote: ")
                self.controle_show.criar_lote_ingresso(show_nome, tipo, quantidade, preco, localizacao)
            case "3":
                show_nome = input("Nome do show: ")
                codigo_ingresso = int(input("Código do ingresso: "))
                self.controle_show.vender_ingresso(show_nome, codigo_ingresso)
            case "4":
                show_nome = input("Nome do show: ")
                self.controle_show.listar_ingressos(show_nome, "Disponível")
            case "5":
                show_nome = input("Nome do show: ")
                self.controle_show.listar_ingressos(show_nome, "Vendido")
            case "6":
                show_nome = input("Nome do show: ")
                self.controle_show.relatorio_financeiro(show_nome)
            case "7":
                self.controle_show.listar_shows()
            case "0":
                print("Saindo...")
                return False
            case _:
                print("Opção inválida. Tente novamente.")
        return True

    def executar(self):
        while True:
            print("\nMenu:")
            print("1. Cadastrar show")
            print("2. Criar lote de ingressos")
            print("3. Vender ingresso")
            print("4. Listar ingressos disponíveis")
            print("5. Listar ingressos vendidos")
            print("6. Gerar relatório financeiro por show")
            print("7. Listar todos os shows")
            print("0. Sair")

            escolha = input("Escolha uma opção: ")

            if not self.escolher_opcao(escolha):
                break


# Execução do programa
if __name__ == "__main__":
    app = Main()
    app.executar()
