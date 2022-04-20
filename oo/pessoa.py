class Pessoa:
    def __int__(self, nome=None, idade=27):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'hello {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = 'Christopher'
    print(p.nome)
    print(p.idade)

