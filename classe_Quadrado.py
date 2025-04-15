""" Crie a classe Quadrado com o atributo tamanho_lado e os métodos mudarValor_lado(), retornar_valor_lado()
e calcular_area(). Instancie um quadrado com lado 5, imprima o tamanho e a área.
Depois, altere o lado para 7 e imprima novamente o tamanho e a nova área."""

class Quadrado:
    def __init__(self, tamanho_lado: float): #construtor
        self.tamanho_lado = tamanho_lado


    def mudarValor_lado(self, novo_lado: float):
        self.tamanho_lado = novo_lado

    def retornar_valor_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
        return self.tamanho_lado ** 2


quadrado = Quadrado(5)

print("-> Tamanho do lado:", quadrado.retornar_valor_lado())
print("-> Área do quadrado:", quadrado.calcular_area())

quadrado.mudarValor_lado(7)
print("-> Novo tamanho do lado:", quadrado.retornar_valor_lado())
print("-> Nova área do quadrado:", quadrado.calcular_area())