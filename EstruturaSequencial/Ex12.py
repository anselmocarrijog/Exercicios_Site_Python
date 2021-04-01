"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
"""
altura = input('Informe a sua altura: ')
a = float(altura)
p = (72.7 * a) - 58
print(f"O peso ideal é {p:.2f}")