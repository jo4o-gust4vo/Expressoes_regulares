import re

class Exercicio07:
    def __init__(self):
        pass

    @classmethod
    def verificar(cls, texto):
        p = re.compile('^@[A-Za-z]+[0-9_]*$')
        if p.search(texto):
            return print('String válida!')
        else:
            return print('String inválida!')

