class Funcionario:
    def __init__(self, nome, salario, imposto):
        self.nome = nome
        self.salario = salario
        self.imposto = imposto

    def getNome(self):
        return self.Nome

    def setNome(self, nome):
        self.nome - nome

    def getSalario(self):
        return self.salario

    def setSalario(self, salario):
        self.salario - salario

    def setImposto(self, imposto):
        self.imposto - imposto

    def SalarioLiquido(self, salario, imposto):
        self.salario = salario
        self.imposto = imposto
        return self.salario - self.imposto

    def AumentoSalario(self, salario, liq , comis):
        valor = liq + (salario * comis / 100)
        return  valor