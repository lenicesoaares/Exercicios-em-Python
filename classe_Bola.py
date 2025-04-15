""" Crie uma classe Bola com atributos cor, circunferencia e material. Implemente os métodos trocaCor(nova_cor) para
alterar a cor e mostraCor() para exibir a cor atual. Instancie uma bola com cor "rosa",
circunferência 30 e material "couro". Em seguida, imprima os atributos, confirme a cor,
 troque a cor para "azul" e mostre a nova cor."""
class Bola:
    def __init__(self, cor: str, circunferencia: int, material: str):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor: str):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor


bola = Bola("rosa", 30, "couro")
print(f"A cor é: {bola.cor}, a circunferencia é: {bola.circunferencia}, e o material é: {bola.material}")

bola = Bola("rosa", 30, "couro")
print(f"Só pra confirmar a cor é: {bola.mostraCor()}")

bola.trocaCor("azul")
print(f"Agora a cor é: {bola.mostraCor()}")