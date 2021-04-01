"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
GanhoHora = float(input('Informe quanto você recebe por hora: '))
HorasTrabalhadas = float(input('Informe as horas trabalhadas no mês: '))
salario = (GanhoHora * HorasTrabalhadas)
print(f'o seu salário este mês é de {salario} reais.')
