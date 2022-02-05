# Crie uma classe Funcionario cujos atributos são nome e e-mail. Guarde as horas trabalhadas em um
# dicionário cujas chaves são o mês em questão e, em outro dicionário, guarde o salário por
# hora relativo ao mês em questão. # Crie um método que retorna o salário mensal do funcionário


class Funcionario:
    def __init__(self, nome, email):
        '''
        Cria um funcionário

        nome : str
            nome do funcionário
        email : str
            email do funcionário
        '''
        self.nome = nome
        self.email = email

        # horas trabalhadas no mes do funcionario
        self.horas_trabalhadas = {}

        # valor da hora naquele mes
        self.salario_hora = {}

    def lancar_horas_mes(self, mes, quantidade_horas):
        '''
        Lança as horas trabalhadas no mês

        mes : str
        quantidade_horas : int

        '''
        self.horas_trabalhadas[mes] = quantidade_horas

    def define_salario_hora_mes(self, mes, valor_salario_hora):
        '''
        Valor da hora trabalhada
        mes : str
        valor_salario_hora : float
        '''

        self.salario_hora[mes] = valor_salario_hora

    def calcula_salario_mes(self, mes):
        '''
        Calcula o salário para o mês vigente

        mes : str
        out : float

        '''
        if (mes in self.salario_hora
                and mes in self.horas_trabalhadas):
            return self.salario_hora[mes] * self.horas_trabalhadas[mes]

        print('Salário ou hora não cadastrada.')
        return 0

thyales = Funcionario(nome='Thyales', email='tfonsecaferreira@gmail.com')
thyales.lancar_horas_mes('12/2021', 160)
thyales.define_salario_hora_mes('12/2021',85)
print(thyales.calcula_salario_mes('12/2021'))

