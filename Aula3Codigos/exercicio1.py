class Livro:

    def __init__(self, titulo, autor, paginas, paginas_lidas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.paginas_lidas = paginas_lidas

    def ler(self, quantidade):
        self.paginas_lidas += quantidade

    def progresso(self):
        porcentagem = ((self.paginas_lidas/self.paginas)*100)

        if porcentagem > 100:
            porcentagem = 100

        print(f"{porcentagem:.2f}%")

livro1 = Livro("Memorias Post", "MachadoAssis", 200, 0)

livro1.ler(250)
livro1.progresso()