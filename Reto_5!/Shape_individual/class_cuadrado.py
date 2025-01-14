from Shape_individual.class_linea import Linea
from Shape_individual.class_rectangulo import Rectangulo

class Cuadrado (Rectangulo):

    regular: bool = True
    def __init__ ( self, p1: tuple ,  p2: tuple, p3: tuple, p4:tuple):

        self.linea1 = Linea(p1,p2)
        Li1 = self.linea1.distancia()
        self.linea2 = Linea(p2,p3)
        Li2 = self.linea2.distancia()
        self.linea3 = Linea(p3,p4)
        Li3 = self.linea3.distancia()
        self.linea4 = Linea(p4,p1)
        Li4 = self.linea4.distancia()
        if Li1==Li2 and Li3 ==Li4:
            if Li1==Li3 and Li2 ==Li4:
                super().__init__(p1,p2,p3,p4)
            else:
                print ("No es un Cuadrado, Organiza mejor los vertices")
        else:
            print ("No es un Cuadrado, Organiza mejor los vertices")


    def ang_inter(self):
        if self.L1 == self.L3 and self.L2 ==self.L4:
            if self.L2== self.L4 and self.L1 ==self.L4:
                return f"es un cuadrado , por lo tanto todos sus angulos interiores miden " \
                   f"90°  por vertice" 
            return "no es un cuadrado"
        else :
            return "no es un cuadrado "  
