# Crie uma classe Bola cujos atributos são cor e raio. Crie um método que imprime a cor da bola.
# Crie um método para calcular a área dessa bola. Crie um método para calcular o volume da bola.
# Crie um objeto dessa classe e calcule a área e o volume, imprimindo ambos em seguida. Obs.:
#
# Área da esfera = 4*3.14*r*r;
#
# Volume da esfera = 4*3.14*r*r*r/3

class Bola:
    def __init__(self, cor, raio):
        '''
        Cria uma Bola:
        :param cor: str
        :param raio: float

        '''
        self.cor = cor
        self.raio = raio

    def imprimir_cor(self):
        '''
        Imprime a cor da Bola
        '''
        print(self.cor)

    def calcular_area(self):
        '''
        Calcula e imprime a área da Bola
        '''

        pi = 3.14
        area = 4*pi*self.raio*self.raio
        print(area)

    def calcular_volume(self):
        '''
        Calcula e imprime o volume da Bola
        '''

        pi = 3.14
        volume = 4 * pi * self.raio * self.raio * self.raio/3
        print(volume)


bola1 = Bola(cor="Branca", raio=2)

bola1.imprimir_cor()
bola1.calcular_area()
bola1.calcular_volume()





