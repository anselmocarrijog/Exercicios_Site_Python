"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
alt = float(input("Informe a sua altura: "))
h = (72.7 * alt) - 58
m = (62.1 * alt) - 44.7

print(f"Se você é homem o seu peso ideal é {h:.2f} e se for mulher é de {m:.2f}")
