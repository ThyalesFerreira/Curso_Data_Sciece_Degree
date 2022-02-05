# 15.	Enunciado
# Crie uma classe Quadrado, filha da classe Retângulo do exercício 2.
class Retangulo:
    def __init__(self, lado_a, lado_b):
        '''
        Cria um retangulo
        :param lado_a: int
        :param lado_b: int
        '''

        self.lado_a = lado_a
        self.lado_b = lado_b

    def area(self):
        '''
        Calcula a área do retangulo
        '''
        return self.lado_a * self.lado_b


class Quadrado(Retangulo):
    '''
    Cria a classe quadrado recebendo como herança a classe Retangulo
    '''
    def __init__(self, lado):

        super().__init__(
            lado_a=lado,
            lado_b=lado
        )

quadrado1 = Quadrado(10)
print(quadrado1.area())