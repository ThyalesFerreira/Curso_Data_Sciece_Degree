# Crie uma classe Cliente cujos atributos são nome, idade e e-mail. Construa um método que imprima as informações tal como abaixo:
# Nome: Fulano de Tal
# Idade: 40
# E-mail: fulano@mail.com

class Cliente:
    def __init__(self,nome,idade,email):
        '''

        :param nome: str
        :param idade: int
        :param email: str
        '''

        self.nome = nome
        self.idade = idade
        self.email = email

    def __repr__(self):
        texto = "Nome: {}\nIdade: {}\nE-mail: {}".format(
            self.nome,
            self.idade,
            self.email
        )
        return texto


cliente1 = Cliente('Fulano de Tal',40,'fulano@mail.com')
print(cliente1)
