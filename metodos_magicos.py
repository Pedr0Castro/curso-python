"""
POO - Métodos mágicos

são todos os métodos que utilizam dunder.

dunder init -

dunder - double underscore

dunder repr - representação do objeto
        def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memória')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += '' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python Rocks! ', 'Geek University', 400)
livro2 = Livro('Inteligencia Artificial em Python', 'Geek University', 350)

print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)

print(livro1 * 3)
