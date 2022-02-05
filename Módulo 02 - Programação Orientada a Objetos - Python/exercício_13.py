# 13.	Enunciado
# Nos exercícios 1, 2, 3, 4 e 6, implemente o método _ repr _ para exibir as informações desejadas de cada uma das classes.

class Bola:
    def __init__(self, cor, raio):
        '''
        Cria uma Bola:
        :param cor: str
        :param raio: float

        '''
        self.cor = cor
        self.raio = raio

    def __repr__(self):
        texto = "A cor da bola é {} e o valor do seu raio é {}".format(
        self.cor,
        self.raio
        )
        return texto


bola1 = Bola(cor="Branca", raio=2)
print(bola1)