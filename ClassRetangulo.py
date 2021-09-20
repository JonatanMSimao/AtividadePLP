import math

class Retangulo:
    def __init__(self, alt, lar):
        self.Largura = lar
        self.Altura = alt

    def getLargura(self):
        return self.Largura
    def getAltura(self):
        return self.Altura
    def setLargura(self, largura):
        self.Largura = largura

    def setAltura(self, altura):
        self.Altura = altura

    def Area(self , alt, lar):
        self.Altura = alt
        self.Largura = lar
        return  self.Altura * self.Largura

    def Perimetro(self , alt, lar):
        self.Altura = alt
        self.Largura = lar
        return 2 * (self.Altura + self.Largura)

    def Diagonal(self, alt , lar):
        self.Altura = alt
        self.Largura = lar
        return math.sqrt((self.Altura * self.Altura) + (self.Largura * self.Largura))