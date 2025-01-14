import math

from Shape_individual.class_linea import Linea
from Shape_individual.class_shape import Shape

class Triangulo(Shape):


    def __init__ ( self, p1: tuple ,  p2: tuple, p3: tuple):
        self.p1 =p1
        self.p2 =p2
        self.p3 =p3

        self.linea1 = Linea(p1,p2)
        self.L1 = self.linea1.distancia()
        self.linea2 = Linea(p2,p3)
        self.L2 = self.linea2.distancia()
        self.linea3 = Linea(p3,p1)
        self.L3 = self.linea3.distancia()

        self.perimetro = (self.L1 + self.L2 + self.L3)
        self.perimetro_2 = self.perimetro /2
        self.area = ((self.perimetro_2)*(self.perimetro_2-self.L1)*\
                     (self.perimetro_2-self.L2)*(self.perimetro_2-self.L3))**0.5
        
        inter_L3 = math.acos((self.L1**2 + self.L2**2 - self.L3**2 )\
                                            /(self.L1*self.L2*2))
        inter_L2 = math.acos((self.L3**2 + self.L1**2 - self.L2**2 )\
                                            /(self.L1*self.L3*2))
        inter_L1 = math.acos((self.L3**2 + self.L2**2 - self.L1**2 )\
                                            /(self.L3*self.L2*2))
        self.inter_L1 = inter_L1 *180 / 3.14159265358979323846264
        self.inter_L2 = inter_L2 *180 / 3.14159265358979323846264
        self.inter_L3 = inter_L3 *180 / 3.14159265358979323846264


    def calcular_perimetro(self):
        if self.area == 0:
            return "...¡¿algo salio mal?! ordena mejor los datos"
        
        return f"El perimetro del triangulo es {self.perimetro}"


    def calcular_area(self):
        if self.area == 0:
            return "...¡¿algo salio mal?! ordena mejor los datos"
        
        return f"El area del triangulo es {self.area}"


    def aristas(self):
        if self.area == 0:
            return "...¡¿algo salio mal?! ordena mejor los datos"
        
        return f"Las aristas del triangulo son \n{self.L1}\n{self.L2}\n{self.L3}"\
                f"\nlista={[self.L1,self.L2,self.L3]}"

    
    def vertices(self):
        if self.area == 0:
            return "...¡¿algo salio mal?! ordena mejor los datos"
        
        return f"Los vertices del triangulo son \n{self.p1} \n{self.p2} \n{self.p3}"\
                f"\nlista={[self.L1,self.L2,self.L3]}"
    
    
    def ang_inter(self):
        if self.area == 0:
            return "...¡¿algo salio mal?! ordena mejor los datos"
        else:
           return f"Aproximadamente los angulos internos son: \n{self.inter_L1}°\n{self.inter_L2}°\n{self.inter_L3}°"


class   Isosceles(Triangulo):
    pass


class Equilateral(Triangulo):
    pass


class Scalene(Triangulo):
    pass


class TriRectangle(Triangulo):
    pass

