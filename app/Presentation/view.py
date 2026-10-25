class LivrariaView:
    def mostrar_menu(self):
        print("\n===== LIVRARIA MVC =====")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Buscar livr o")
        print("4. Excluir livro")
        print("0. Sair")
        return input("Escolha uma opção: ").strip()

    def solicitar_livro(self):
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        preco = float(input("Preço (R$): ").replace(",", "."))

        if not titulo or not autor:
            raise ValueError("Título e autor são obrigatórios.")

        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")

        return titulo, autor, preco

    def solicitar_id(self):
        return int(input("Digite o ID do livro: "))

    def solicitar_busca(self):
        return input("Digite o título para pesquisar: ").strip()

    def mostrar_livros(self, livros):
        if not livros:
            print("\nNenhum livro encontrado.")
            return

        print("\n===== CATÁLOGO =====")
        for livro in livros:
            print(
                f"ID: {livro.id} | "
                f"Título: {livro.titulo} | "
                f"Autor: {livro.autor} | "
                f"Preço: R$ {livro.preco:.2f}"
            )

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_erro(self, mensagem):
        print(f"Erro: {mensagem}")