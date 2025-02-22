class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print(f'Olá meu nome é {self.nome} e tenho')
        print(f'{self.idade} anos, e tenho')
        print(f'{self.altura} tudo isso de altura')

p1 = Pessoa("Lucas", 19, "1.65")
p1.apresentar()