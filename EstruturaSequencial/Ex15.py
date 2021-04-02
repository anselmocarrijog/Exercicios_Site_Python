"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
=====================================================================================================
A - salário bruto.
B - quanto pagou ao INSS.
C - quanto pagou ao sindicato.
D - o salário líquido.
E - calcule os descontos e o salário líquido, conforme a tabela abaixo:
=====================================================================================================
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
=====================================================================================================
"""
valor_horas = float(input("Informe o quanto você ganha por hora: "))
horas_trabalhadas = float(input("Infome quantas horas trabalhadas no mês: "))

# Variáveis
salario_bruto = valor_horas * horas_trabalhadas
ir = salario_bruto * (11 / 100)
inss = salario_bruto * (8 / 100)
sindicato = salario_bruto * (5 / 100)
descontos = (ir + inss + sindicato)
salario_liquido = salario_bruto - descontos
print("Seu salário bruto foi de {:.2f} Reais. O desconto do imposto de renda foi de {:.2f}, o Inss de {:.2f} e sindicato de {:.2f}.\n"
      "O seu salário líquido é de {:.2f}".format(salario_bruto,ir, inss, sindicato, salario_liquido))

