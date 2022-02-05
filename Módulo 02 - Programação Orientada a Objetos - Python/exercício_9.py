# 9.	Enunciado
# Com base no exercício anterior, crie um sistema de cadastro e a classe Cliente.
# Seu programa deve perguntar se o usuário quer cadastrar um novo cliente, alterar um cadastro ou sair.
# Dica: Você pode fazer esse exercício criando uma classe Sistema, que irá controlar o sistema de cadastros.
# Essa classe deve ter o atributo cadastro e os métodos para imprimir os cadastrados, cadastrar um novo cliente,
# alterar um cadastro ou sair.

class Cliente:
    def __init__(self,nome,idade,email):
        '''
        Cria um novo cliente
        :param nome: str
        :param idade: int
        :param email: str
        '''

        self.nome = nome
        self.idade = idade
        self.email = email

    def imprimir_dados(self):
        print("Nome:",self.nome,"\n","Idade:",self.idade,"\n","E-mail:",self.email)


class Sistema:
    def __init__(self):
        self.lista_clientes = []
        '''
        Sistema que controla o cadastro de clientes
        '''

    def cadastrar_cliente(self):
        '''
        Realiza um cadastro de um novo cliente
        '''

        resposta = input("Deseja cadastrar um novo cliente? Digite 'Sim' ou 'Não'")

        if resposta == 'Sim':
            nome = input("Digite o nome do cliente:")
            idade = input("Digite a idade do cliente:")
            email = input("Digite o email do cliente:")

            cliente = Cliente(nome=nome, idade=idade, email=email)

        self.lista_clientes.append(cliente)

    def remover_cliente(self,cliente):
        '''
        Remove um cliente da lista de clientes
        '''
        self.lista_clientes.remove(cliente)

    def imprimir_cadastrados(self):
        '''
        Imprime os clientes cadastrados
        '''

        for cliente in self.lista_clientes:
            print(cliente.nome,",", cliente.idade,",",cliente.email)

sistema = Sistema()
cliente1 = Cliente('Fulano de Tal',40,'fulano@mail.com')

sistema.cadastrar_cliente()
sistema.imprimir_cadastrados()



