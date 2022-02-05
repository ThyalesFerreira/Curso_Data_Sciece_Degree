# 5.	Crie uma classe ControleRemoto cujo atributo é televisão (isso é, recebe um objeto da classe do exercício 4).
# Crie métodos para aumentar/diminuir volume, trocar o canal e sintonizar um novo canal, que adiciona um novo canal
# à lista de canais (somente se esse canal não estiver nessa lista).

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

    def aumentar_volume(self, x):
        '''
        Aumenta o volume da televisão
        :param x: int
        '''

        self.volume = self.volume + x
        if self.volume > 100:
            self.volume = 100
        return self.volume

    def diminuir_volume(self, x):
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


class ControleRemoto:
    def __init__(self, nome):

        '''
        Cria um controle Remoto
        :param nome: str
        '''

        self.__nome = nome
        self.__controle_remoto = None

    @property
    def nome(self):
        return self.__nome

    @property
    def controle_remoto(self):
        return self.__controle_remoto

    @controle_remoto.setter
    def controle_remoto(self,controle_remoto):
        self.__controle_remoto = controle_remoto


televisao1 = Televisor(
            fabricante='Sansumg',
            modelo='Full HD',
            canal_atual=7,
            volume=25
            )

controle1 = ControleRemoto(nome='Controlex')

# controle1 = ControleRemoto(televisao=televisao1)
# print(controle1)
# # controle1.aumentar_volume(10)

controle1.controle_remoto = televisao1
print(controle1.controle_remoto.fabricante)
print(controle1.controle_remoto.aumentar_volume(5))
