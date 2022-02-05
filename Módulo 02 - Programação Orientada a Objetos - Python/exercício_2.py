# 2.	Crie uma classe Retângulo cujos atributos são lado_a e lado_b. Crie um método para calcular a área desse retângulo.
# Crie um objeto dessa classe e calcule a área e a imprima em seguida.

class Retangulo:
    def __init__(self, lado_a, lado_b):
        '''
        Cria um retãngulo.
        :param lado_a: int
        :param lado_b: int

        '''

        self.lado_a = lado_a
        self.lado_b = lado_b

    def calcula_area(self):
        '''
        Calcula e retorna a área do retangulo

        '''

        area = self.lado_a * self.lado_b
        return area

retangulo1 = Retangulo(lado_a=9,lado_b=8)

print(retangulo1.calcula_area())
