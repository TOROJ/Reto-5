
from Shape_individual.class_linea import Linea
from Shape_individual.class_shape import Shape


class Rectangulo (Shape):


    def __init__ ( self, p1: tuple ,  p2: tuple, p3: tuple, p4:tuple):
        self.p1 =p1
        self.p2 =p2
        self.p3 =p3
        self.p4 =p4

        self.linea1 = Linea(p1,p2)
        self.L1 = self.linea1.distancia()
        self.linea2 = Linea(p2,p3)
        self.L2 = self.linea2.distancia()
        self.linea3 = Linea(p3,p4)
        self.L3 = self.linea3.distancia()
        self.linea4 = Linea(p4,p1)
        self.L4 = self.linea4.distancia()

        if self.L1 == self.L3 and self.L2 ==self.L4:
            print (f"sus lados son  {self.L1, self.L2,self.L3,self.L4}")
        else:
            return "no es un rectangulo, por favor organiza los datos de una forma correcta"
    

    def calcular_perimetro(self):
        if self.L1 == self.L3 and self.L2 ==self.L4:
            return f"Su perimetro es {(self.L1 + self.L2 )*2} unidades"
        else :
            return "no es un rectangulo"
    

    def calculara_area(self):
        if self.L1 == self.L3 and self.L2 ==self.L4:
            return f"Su area son {(self.L1 * self.L2 )} unidades"
        else :
            return "no es un rectangulo, por favor organiza los datos de una forma correcta"      
    

    def vertices( self):
        if self.L1 == self.L3 and self.L2 ==self.L4:
            return f"Sus vertices son los puntos: \nPunto 1: {self.L1} \nPunto 2: {self.L2} "\
                f"\nPunto 3: { self.L3} \nPunto 4: {self.L4}\nlista={[self.L1,self.L2,self.L3,self.L4]}"
        else :
            return "no es un rectangulo, por favor organiza los datos de una forma correcta"
        

    def aristas(self):
        if self.L1 == self.L3 and self.L2 ==self.L4:
            return f"Sus aristas son las lineas:\nLinea 1: {self.L1} unidades\nLinea 2: {self.L2} unidades"\
                   f"\nLinea 3: {self.L3} unidades\nLinea 4: { self.L4} unidades"\
                   f"\nlista={[self.L1,self.L2,self.L3,self.L4]}"
        else :
            return "no es un rectangulo, por favor organiza los datos de una forma correcta"
 
        
    def ang_inter(self):
        if self.L1 == self.L3 and self.L2 ==self.L4:
            return "es un rectangulo , por lo tanto todos sus angulos interiores miden " \
                    "90°  por vertice"
        else :
            return "no es un rectangulo, por favor organiza los datos de una forma correcta"    
