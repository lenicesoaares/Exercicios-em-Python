"""
Classe Retângulo: Crie uma classe que modele um retângulo:

- Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
- Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
- Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local.
- Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""

class Retangulo:
    def __init__(self, LadoA: float, LadoB: float):
        self.LadoA = LadoA
        self.LadoB = LadoB

    def trocaValor(self, muda_valor1: float, muda_valor2: float):
        self.LadoA = muda_valor1
        self.LadoB = muda_valor2
        return

    def mostraValor(self):
        return self.LadoA, self.LadoB

    def calcular_area(self):
        return self.LadoA * self.LadoB

    def calcular_perimetro(self):
        return 2 * (self.LadoA + self.LadoB)

    def calcular_pisos_rodapes(self, area, piso_area, rodape_linha):
        quantidade_pisos = area / piso_area
        quantidade_rodape = 2 * (self.LadoA + self.LadoB) / rodape_linha
        return quantidade_pisos, quantidade_rodape

LadoA = float(input("- Informe o valor do Lado A: "))
LadoB = float(input("- Informe o valor do Lado B: "))

retangulo = Retangulo(LadoA, LadoB)

area = retangulo.calcular_area()
perimetro = retangulo.calcular_perimetro()

piso_area = float(input("- Informe a área de um piso (em metros quadrados): "))
rodape_linha = float(input("- Informe a medida de um rodapé (em metros): "))

quantidade_pisos, quantidade_rodape = retangulo.calcular_pisos_rodapes(area, piso_area, rodape_linha)

print(f">> Área do retângulo: {area} m²")
print(f">> Perímetro do retângulo: {perimetro} m")
print(f">> Quantidade de pisos necessários: {quantidade_pisos}")
print(f">> Quantidade de rodapés necessários: {quantidade_rodape}")
