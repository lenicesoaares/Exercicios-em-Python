"""Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha. """

#O range(start, stop) cria uma sequência de números começando de start até, mas não incluindo, stop.
#O +1 é necessário porque o valor final do range não é incluído.
def linhas_diferentes(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end="   ")
        print()

print(">> ESCOLHA UM NÚMERO (PRA SER MAIS LEGAL, ESCOLHA ACIMA DE 2 <<")
numero = int(input(">> Digite aqui o número: "))

linhas_diferentes(numero)

