"""Faça uma função que imporima o padrão
           *

        *.* *

     * * * * *

  * * * * * * *

* * * * * * * * *
a função deve receber o tamanho da linha maior """
def estrelinha(tamanho):
    for i in range(1, tamanho + 1):
        linha = " " * (tamanho - i)
        for j in range(1, i * 2, 2):
            linha = linha + "* "
        print(linha)

print(">> MONTE SUA ÁRVORE DE NATAL <<")
tamanho = int(input(">> Digite um número que você quer para sua árvore de Natal: "))
estrelinha(tamanho)

