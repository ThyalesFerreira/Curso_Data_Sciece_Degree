# 4. Crie uma classe Televisor cujos atributos são:
# a. fabricante;
# b. modelo;
# c. canal atual;
# d. lista de canais; e
# e. volume.
# Faça métodos para aumentar/diminuir volume, trocar o canal e sintonizar um novo canal, que adiciona um novo canal à lista de canais
# (somente se esse canal não estiver nessa lista). No atributo lista de canais, devem estar armazenados todos os canais já sintonizados dessa TV.
# Obs.: O volume não pode ser menor que zero e maior que cem; só se pode trocar para um canal que já esteja na lista de canais.

class Televisor:
    def __init__(self, fabricante, modelo, canal_atual, volume):
        '''

        Cria uma televisão
        :param fabricante: str
        :param modelo: str
        :param canal_atual: int
        :param volume: int
        '''

        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = canal_atual
        self.volume = volume
        self.lista_canais = [1,2,3,4,5,6,7,8,9,10]


    def aumenta_volume(self,x):
        '''
        Aumenta o volume da televisão
        :param x: int
        '''

        self.volume = self.volume + x
        if self.volume > 100:
            self.volume = 100
        return self.volume

    def diminui_volume(self, x):
        '''
        Diminui o volume da televisão
        :param x: int
        '''

        self.volume = self.volume - x
        if self.volume < 0:
            self.volume = 0
        return self.volume

    def trocar_canal(self, novo_canal):
        '''
        Troca o canal da televisão verificando se este canal está no pacote do cliente
        :param novo_canal: int

        '''

        if novo_canal not in self.lista_canais:
            print("Este canal não pertence ao seu pacote")
        else:
            self.canal_atual = novo_canal


    def adicionar_canal(self, add_canal):
        '''
        Adiciona canal no pacote de canais do cliente
        :param add_canal: int

        '''
        self.lista_canais.append(add_canal)
        print("Canal adicionado com sucesso!")


televisao1 = Televisor(
            fabricante='Sansumg',
            modelo='Full HD',
            canal_atual=7,
            volume=25
            )

print(televisao1.aumenta_volume(10))
print(televisao1.volume)
(televisao1.trocar_canal(90))
print(televisao1.canal_atual)