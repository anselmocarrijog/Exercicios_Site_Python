"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A: o produto do dobro do primeiro com metade do segundo .
B: a soma do triplo do primeiro com o terceiro.
C: o terceiro elevado ao cubo.
"""
n1 = int(input('Informe o 1° número inteiro: '))
n2 = int(input('Informe o 2° número inteiro: '))
n3 = float(input('Informe o número real: '))

print('O produto do dobro do primeiro com metade do segundo é:\n',
      (n1 * 2) + (n2 / 2))
print(20 * '===')
print('A soma do triplo do primeiro com o terceiro é:\n',
      (3 * n1) + n3)
print(20 * '===')
print('O terceiro elevado ao cubo é:\n',
      (n3 ** 3))
print(20 * '===')