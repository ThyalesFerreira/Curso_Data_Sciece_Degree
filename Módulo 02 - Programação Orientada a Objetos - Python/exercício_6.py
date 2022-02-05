# 6.	O módulo time possui a função time.sleep(x), que faz seu programa “dormir” por x segundos. Utilizando essa função,
# crie uma classe Cronômetro e faça um programa que cronometre o tempo.

import time

class Cronometro:
    def __init__(self, marca):
        '''
        Cria um cronômetro
        :param marca str
        '''

        self.marca = marca

    def cronometrar(self, tempo):
        '''
        Recebe o tempo informado e apresenta mensagem após este tempo ser decorrido
        :param tempo:int
        :return:
        '''

        time.sleep(tempo)
        print(f'Tempo de {tempo} segundos decorrido com sucesso')

cronometro = Cronometro(marca='xpto')
cronometro.cronometrar(5)

