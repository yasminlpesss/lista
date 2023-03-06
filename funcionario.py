nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))

if salario <= 1500:
    aumento = salario * 0.10
else:
    aumento = salario * 0.05

novo_salario = salario + aumento
diferenca = novo_salario - salario

print("Novo salário de", nome, ": R$ {:.2f}".format(novo_salario))
print("Aumento de R$ {:.2f}".format(aumento))
print("Diferença em relação ao salário antigo: R$ {:.2f}".format(diferenca))
