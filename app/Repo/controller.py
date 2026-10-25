from model import LivrariaModel
from app.Presentation.view import LivrariaView


class LivrariaController:
    def __init__(self):
        self.model = LivrariaModel()
        self.view = LivrariaView()

    def executar(self):
        while True:
            opcao = self.view.mostrar_menu()

            try:
                if opcao == "1":
                    self.cadastrar()
                elif opcao == "2":
                    self.listar()
                elif opcao == "3":
                    self.buscar()
                elif opcao == "4":
                    self.excluir()
                elif opcao == "0":
                    self.view.mostrar_mensagem(
                        "Aplicativo    encerrado."
                    )
                    break
                else:
                    self.view.mostrar_erro(
                        "Opção inválida."
                    )

            except (ValueError, EOFError) as erro:
                self.view.mostrar_erro(str(erro))

    def cadastrar(self):
        titulo, autor, preco = self.view.solicitar_livro()

        livro = self.model.cadastrar_livro(
            titulo, autor, preco
        )

        self.view.mostrar_mensagem(
            f"Livro '{livro.titulo}' cadastrado "
            f"com sucesso! ID: {livro.id}"
        )

    def listar(self):
        livros = self.model.listar_livros()
        self.view.mostrar_livros(livros)

    def buscar(self):
        termo = self.view.solicitar_busca()
        livros = self.model.buscar_livros(termo)
        self.view.mostrar_livros(livros)

    def excluir(self):
        livro_id = self.view.solicitar_id()

        if self.model.excluir_livro(livro_id):
            self.view.mostrar_mensagem(
                "Livro excluído com sucesso."
            )
        else:
            self.view.mostrar_erro(
                "Livro não encontrado."
            )