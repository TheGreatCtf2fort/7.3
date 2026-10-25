from dataclasses import dataclass

@dataclass
class Livro:
    id: int
    titulo: str
    autor: str
    preco: float


class LivrariaModel:
    def __init__(self):
        self.livros = []
        self.proximo_id = 1

    def cadastrar_livro(self, titulo, autor, preco):
        livro = Livro(
            id=self.proximo_id,
            titulo=titulo,
            autor=autor,
            preco=preco
        )
        self.livros.append(livro)
        self.proximo_id += 1
        return livro

    def listar_livros(self):
        return self.livros.copy()

    def buscar_livros(self, termo):
        termo = termo.casefold()
        return [
            livro for livro in self.livros
            if termo in livro.titulo.casefold()
        ]

    def excluir_livro(self, livro_id):
        for livro in self.livros:
            if livro.id == livro_id:
                self.livros.remove(livro)
                return True
        return False