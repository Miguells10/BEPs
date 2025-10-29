from Bep19.Ingresso import Ingresso
from Bep19.IngressoCamarote import IngressoCamarote
from Bep19.Show import Show
from Bep19.tratamento import PrecoInvalidError


class ControleShow:
    def __init__(self):
        self.shows = []


    def cadastrar_show(self, nome, data, local):
        show = Show(nome, data, local)
        self.shows.append(show)
        print(f"Show '{nome}' cadastrado com sucesso!")


    def buscar_show(self, nome):
        for show in self.shows:
            if show.nome.lower() == nome.lower():
                return show
        print(f"Show '{nome}' não encontrado.")
        return None

    def criar_lote_ingresso(self, show_nome, tipo, quantidade, preco, localizacao=None):
        show = self.buscar_show(show_nome)
        if not show:
            return

        try:
            if tipo.lower() not in ["pista", "camarote"]:
                raise ValueError("Tipo de ingresso inválido. Use 'pista' ou 'camarote'.")

            if preco <= 0:
                raise PrecoInvalidError("O preço deve ser maior que zero.")

            for _ in range(quantidade):
                if tipo.lower() == "pista":
                    ingresso = Ingresso(preco)
                else:
                    ingresso = IngressoCamarote(preco, localizacao)
                show.adicionar_ingresso(ingresso)

            print(f"{quantidade} ingressos do tipo '{tipo}' criados para o show '{show_nome}'.")

        except PrecoInvalidError as e:
            print(f"Erro: {e}")
        except ValueError as e:
            print(f"Erro: {e}")


    def vender_ingresso(self, show_nome, codigo_ingresso):
        show = self.buscar_show(show_nome)
        if not show:
            return

        for ingresso in show.lista_ingressos:
            if ingresso.codigo == codigo_ingresso:
                if ingresso.status == "Disponível":
                    ingresso.vender()
                    print(f"Ingresso {codigo_ingresso} vendido com sucesso!")
                    return
                else:
                    print("Esse ingresso já foi vendido.")
                    return

        print("Ingresso não encontrado.")


    def listar_shows(self):
        if not self.shows:
            print("Nenhum show cadastrado.")
        else:
            print("\n📅 Lista de Shows:")
            for show in self.shows:
                print(show)


    def listar_ingressos(self, show_nome, status):
        show = self.buscar_show(show_nome)
        if not show:
            return

        if status.lower() == "disponível":
            show.listar_ingressos_disponiveis()
        elif status.lower() == "vendido":
            show.listar_ingressos_vendidos()
        else:
            print("Status inválido. Use 'disponível' ou 'vendido'.")

    def relatorio_financeiro(self, show_nome):
        show = self.buscar_show(show_nome)
        if not show:
            return

        total = show.calcular_total_arrecadado()
        print(f"\nTotal arrecadado com o show '{show_nome}': R$ {total:.2f}")
