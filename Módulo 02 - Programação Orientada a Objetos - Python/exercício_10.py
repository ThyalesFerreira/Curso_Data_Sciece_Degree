# Crie uma classe ContaCorrente com os atributos cliente (que deve ser um objeto da classe Cliente) e saldo.
# Crie métodos para depósito, saque e transferência. Os métodos de saque e transferência devem verificar se é
# possível realizar a transação


class Cliente:
    def __init__(self, nome, idade, email):
        '''
        Cria um novo cliente
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


class ContaCorrente:
    def __init__(self, cliente, saldo=0):
        '''
        Cria uma conta corrente para o cliente com saldo inicial zero
        '''
        self.cliente = cliente
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def __repr__(self):
        texto = self.cliente.__repr__() + "Saldo: {}".format(
            self.__saldo
        )

    def saque(self, valor):
        '''
        Realiza um saque na conta corrente do cliente
        :param valor: float
        '''
        if self.__saldo - valor >= 0:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente.')

    def deposito(self, valor):
        '''
        Deposita um valor na conta do cliente
        :param valor: float

        '''
        self.__saldo += valor

    def transferencia(self, other, valor):
        '''
        Realiza uma transferência entre a conta do cliente e outra conta passada por parâmetro

        :return:
        '''
        if self.__saldo - valor >= 0:
            self.__saldo -= valor
            other.__saldo += valor
        else:
            print('Saldo insuficiente.')


thyales = Cliente(
    nome='Thyales',
    idade=33,
    email='tfonsecaferreira@gmail.com'
)
karina = Cliente(
    nome='Karina',
    idade=32,
    email='karina@gmail.com'
)

conta_thyales = ContaCorrente(thyales, saldo=1000)
conta_karina = ContaCorrente(karina, saldo=500)

conta_thyales.saque(300)

conta_thyales.transferencia(conta_karina, 100)
conta_thyales.deposito(150)
print(conta_thyales.saldo)
print(conta_karina.saldo)



