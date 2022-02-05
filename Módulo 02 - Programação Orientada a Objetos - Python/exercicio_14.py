# Faça uma classe ContaVip que difere da ContaCorrente por ter cheque especial(novo atributo) e é filha da classe ContaCorrente.Você
# precisa implementar os métodos para saque, transferência ou depósito?

class Cliente:
    def __init__(self, nome, idade, email):
        '''
        Cria um cliente
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
        Cria uma conta corrente com saldo inicial igual a zero
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
        :param valor: int
        '''
        if self.__saldo - valor >= 0:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente.')

    def deposito(self, valor):
        '''
        Deposita um valor na conta corrente do cliente
        :param valor: int
        '''
        self.__saldo += valor

    def transferencia(self, other, valor):
        '''
        Realiza uma transferência entre contas
        :param valor: int
        '''
        if self.__saldo - valor >= 0:
            self.__saldo -= valor
            other.__saldo += valor
        else:
            print('Saldo insuficiente.')


class ContaVip(ContaCorrente):
    def __init__(self, cliente, saldo=0, cheque_especial=0):
        '''
        Cria uma conta corrente vip com atributos herdados da classe ContaCorrente
        '''
        super().__init__(cliente, saldo)
        self.cheque_especial = cheque_especial

    def saque(self, valor):
        '''
        Realiza um saque na conta vip
        :param valor: int
        '''
        if ((self.saldo + self.cheque_especial) - valor >= 0):
            self.deposito(-valor)
        else:
            print('Saldo insuficiente.')

    def transferencia(self, other, valor):
        '''
        Realiza uma transferência entre contas
        '''

        if ((self.saldo + self.cheque_especial) - valor >= 0):
            self.deposito(-valor)
            other.deposito(valor)
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
conta_karina = ContaVip(karina)

conta_thyales.saque(300)

conta_thyales.transferencia(conta_thyales, 100)

print(conta_thyales.saldo)
conta_thyales.deposito(200)
print(conta_karina.saldo)
conta_karina.transferencia(conta_thyales, 30)

