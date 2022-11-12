import math

class Poligono:
    def __init__(self): 
        self.pontos = []

    def addPontos(self, x, y):
        self.pontos.append((x,y))

    def perimetro(self):
        perimetro = 0
        n = len(self.pontos)
        for i in range(n):
            x1 = self.pontos[(i+1)%n][0]
            y1 = self.pontos[(i+1)%n][1]
            x0 = self.pontos[i][0]
            y0 = self.pontos[i][1]
            soma = math.sqrt((x1-x0)**2 + (y1 - y0)**2)
            perimetro += soma
        
        return perimetro
    
    def area(self):
        area = 0
        n = len(self.pontos)
        for i in range(n):
            x1 = self.pontos[(i+1)%n][0]
            y1 = self.pontos[(i+1)%n][1]
            x0 = self.pontos[i][0]
            y0 = self.pontos[i][1]
            soma = ((x0*y1) - (x1*y0))
            area += soma

        return area