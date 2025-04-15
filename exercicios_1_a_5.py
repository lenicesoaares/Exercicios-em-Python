"""
Faça uma função  que mostre a mensagem "Alo mundo" na tela.
Faça uma função  que peça um número e então mostre a mensagem O número informado foi [número].
Faça uma função  que peça dois números e imprima a soma.
Faça uma função  que peça as 4 notas bimestrais e mostre a média.
Faça uma função  que converta metros para centímetros."""

print("> Faça uma função  que mostre a mensagem 'Ola mundo' na tela\n")
def olamundo():
    print("- Ola mundooo!!!")


olamundo()

print("-" * 30)

print("> Faça uma função  que peça um número e então mostre a mensagem O número informado foi [número]\n")
def numerouti():
    numero = int(input("Digite um número aqui: "))
    print(f"O número que você digitou foi {numero}")

numerouti()

print("-" * 30)

print("> Faça uma função  que peça dois números e imprima a soma\n")
def somauti():
    numero1 = int(input("- Digite o primeiro número que você quer somar: "))
    numero2 = int(input("- Digite o segundo número que você quer somar: "))
    soma = numero1 + numero2
    print(f"--> A soma do {numero1} com o {numero2} foi {soma}")

somauti()

print("-" * 30)

print("> Faça uma função  que peça as 4 notas bimestrais e mostre a média\n")
def notas():
    total = 0
    for x in range(4):
        nota = float(input(f"Digite a nota {x + 1}: "))
        total += nota
    media = total / 4
    print(f"--> A média final do bimestre foi {media}")

notas()

print("-" * 30)

print("> Faça uma função  que converta metros para centímetros\n")
def converte():
    metros = float(input("Digite um valor em metros para converter em centímetros: "))
    cent = metros * 100
    print(f"--> O valor que você digitou fica {cent} centímetros")

converte()

print("-" * 30)

def notavalida():
    total = 0
    for x in range(4):
        nota = float(input(f"Digite a nota {x+1} de 0 a 20: "))
        if 0 <= nota <= 20:
            total = total + nota
        else:
            print("Nota inválida! A nota será desconsiderada, tente novamente mais tarde, beijos.")
            return
    media = total / 4
    print(f"A média das notas é: {media}")

notavalida()

