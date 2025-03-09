class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True  

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' já está emprestado.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print(f"O livro '{self.titulo}' já estava disponível.")

    def __str__(self):
        return f"{self.titulo} ({self.ano}) - {self.autor} - Disponível: {'Sim' if self.disponivel else 'Não'}"


livro1 = Livro("Diário De Um Mago", "Paulo Coelho", 1998)
livro2 = Livro("O Estilo de Jesus, Declínio de um Homem", "Jonas Ribeiro", 2007)


print(livro1)
print(livro2)

livro1.emprestar()
livro1.emprestar() 
livro1.devolver()
livro1.devolver()