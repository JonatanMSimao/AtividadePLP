from function import limpar
from function import lin
from function import tempo
from ClassFuncionario import Funcionario
from ClassRetangulo import Retangulo


opcao = 1
while (opcao != 0):

    lin()
    print("*************** 1ª LISTA DE ATIVIDADES – PLP ***************")
    lin()
    print(" PARA QUESTÃO 01 - Digite 1")
    print(" PARA QUESTÃO 02 - Digite 2")
    print(" PARA QUESTÃO 03 - Digite 3")
    print(" PARA QUESTÃO 04 - Digite 4")
    print(" PARA QUESTÃO 05 - Digite 5")
    print(" PARA FINALIZAR  - Digite 0")
    lin()
    opcao = int(input("Selecione a Questão: "))

    limpar()

    if (opcao == 1):
        lin()
        print("************* QUESTÂO 1 - A Pessoa Mais Velha **************")
        lin()
        print("Dados da primeira pessoa: ")
        p1 = input("Nome: ")
        i1 = int(input("Idade: "))
        print("Dados da Segunda pessoa: ")
        p2 = input("Nome: ")
        i2 = int(input("Idade: "))

        if (i1 > i2):
            print("Pessoa Mais Velha: {}".format(p1))
        else:
            print("Pessoa Mais Velha: {}".format(p2))

        print("")
        tempo()

    elif (opcao == 2):
        lin()
        print("********** QUESTÂO 2 - Salário Médio Funcionários *********")
        lin()
        print("Digite o nome do primeiro funcionairo: ")
        p1 = input("Nome: ")
        s1 = float(input("Salário: "))
        print("Digite o nome do Segundo funcionairo: ")
        p2 = input("Nome: ")
        s2 = float(input("Salário: "))

        media = (s1 + s2) / 2

        print("Salário médio =  {}".format(media))

        print("")
        tempo()

    elif (opcao == 3):

        lin()
        print("************* QUESTÂO 3 - Medidas do Triângulo *************")
        lin()
        print("Digite a Largura e em seguida a Altura: ")
        L1 = float(input("Largura: "))
        A1 = float(input("Altura: "))

        retangulo = Retangulo(A1, L1)

        area = retangulo.Area(A1, L1)
        perimetro = retangulo.Perimetro(A1, L1)
        diagonal = retangulo.Diagonal(A1, L1)

        print("Área: {}".format(area))
        print("Perímetro: {}".format(perimetro))
        print("Diagonal: {}".format(diagonal))

        print("")
        tempo()

    elif (opcao == 4):
        
        lin()
        print("********* QUESTÂO 4 - Impostos e Aumento de Salário ********")
        lin()

        print("Digite os Dados do Funcionário")
        nome = input("Nome: ")
        salario = float(input("Salário Bruto: "))
        imposto = float(input("Imposto: "))
        funcionario1 = Funcionario(nome, salario, imposto)
        liquido = funcionario1.SalarioLiquido(salario, imposto)
        print(" ")
        print("Funcionário : {} , Salário Líquido R$ {}".format(nome, liquido))
        comis = float(input("porcentagem de aumento: "))
        aument = funcionario1.AumentoSalario(salario, liquido, comis)

        print("Dados Atualizados : {} R$ {}".format(nome, aument))

        print("")
        tempo()

    elif (opcao == 5):

        lin()
        print("************ QUESTÂO 5 - Aprovado ou Reprovado *************")
        lin()
        nome = input("Nome do Aluno: ")
        nota1 = float(input("Primeira nota : "))
        nota2 = float(input("Segunda nota : "))
        nota3 = float(input("Terceira nota : "))

        notas = (nota1 + nota2 + nota3)
        print("")
        vb = 60.0
        vr = vb - notas
        if (notas >= vb):
            print("Nota final = {:.2f}".format(notas))
            print("Aprovado")
        else:
            print("Nota final = {:.2f}".format(notas))
            print("Reprovado")
            print("Faltaram {:.2f} pontos".format(vr))

        print("")
        tempo()

    elif (opcao == 0):
        break
    else:
        print("Questão não existe! ")
        tempo()
