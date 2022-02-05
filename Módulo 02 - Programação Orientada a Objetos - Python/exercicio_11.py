# Encapsulamento
# Exercícios
# da
# lista: 8, 9, 10, 12, 13.
#
# Crie uma classe Fração cujos atributos são numerador(número de cima) e denominador(número de baixo). Implemente os
# métodos de adição, subtração, multiplicação, divisão que retornam objetos do tipo Fração. Implemente também o método _repr_.
# Implemente métodos para comparação: igualdade( ==) e desigualdades( !=, <=, >=, < e >).


class Fracao:
    def __init__(self, numerador, denominador):
        '''
        Cria uma fração
        :param numerador: float
        :param denominador: float
        '''

        if (denominador == 0):
            raise ValueError('Denominador não pode ser igual a 0.')# cria uma mensagem de erro na tela

        self.numerador = numerador
        self.denominador = denominador

    def valor(self):
        '''
        Calcula o resultado da fração
        :return:
        '''
        return self.numerador / self.denominador

    def __repr__(self):
        return f'{self.numerador}/{self.denominador}'

    def __add__(self, other):
        '''
        Soma duas frações
        :param other: float

        '''
        num = self.numerador * other.denominador + \
              self.denominador * other.numerador

        den = self.denominador * other.denominador

        return Fracao(num, den)

    def __sub__(self, other):
        '''
        Subtrai duas frações
        :param other: float

        '''
        num = self.numerador * other.denominador - \
              self.denominador * other.numerador

        den = self.denominador * other.denominador

        return Fracao(num, den)

    def __mul__(self, other):
        '''
        Multoplica duas frações
        :param other: float

        '''
        num = self.numerador * other.numerador
        den = self.denominador * other.denominador

        return Fracao(num, den)

    def __truediv__(self, other):
        num = self.numerador * other.denominador
        den = self.denominador * other.numerador

        return Fracao(num, den)

    def __eq__(self, other):
        '''
        Verifica se as frações são iguais
        '''
        return self.valor() == other.valor()

    def __lt__(self, other):
        '''
        Verifica se a fração é menor que a outra passada por parâmetro
        '''
        return self.valor() < other.valor()
        
    def __le__(self, other):
        '''
        Verifica se a fração é menor ou igual a outra passada por parâmetro
        '''
        
        return self.valor() <= other.valor()

    def __gt__(self, other):
        '''
        Verifica se a fração é maior que a outra passada por parâmetro
        '''
        return self.valor() > other.valor()

    def __ge__(self, other):
        '''
        Verifica se a fração é maior ou igual a outra passada por parâmetro
        '''
        return self.valor() >= other.valor()

fracao1 = Fracao(1, 2)
fracao2 = Fracao(5, 2)
fracao3 = Fracao(1, 2)

print(fracao1 + fracao2 + fracao3)

fracao4 = fracao1 - fracao2

print(fracao1 * fracao2*fracao3)

print(fracao1/fracao2)

print(fracao1 == fracao3)

print(fracao1 < fracao3)

print(fracao1 <= fracao3)

print(fracao1 > fracao3)

print(fracao1 >= fracao3)