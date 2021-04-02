"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
area = float(input("Informe o tamanho da área a ser pintada: "))
quantidade_litros = area / 3
total_latas = quantidade_litros / 18
precol = 80
total = precol * total_latas

print("A quantidade em litros é de {:.2f}, total de latas é de {:.2f} e o valor total a ser pago é de {:.2f} Reais.".format(quantidade_litros,total_latas,total))

