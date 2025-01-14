def main():
    from shape.total import Rectangulo,Cuadrado,Triangulo

    triangulos = Triangulo ((0,0),(6,0),(3,5))
    rectangulos= Rectangulo((2,0),(0,0),(0,3),(2,3))    
    cuadrados = Cuadrado((2,0),(0,0),(0,2),(2,2))
    print (rectangulos.aristas())
    print (rectangulos.vertices())
    print (rectangulos.calculara_area())
    print (rectangulos.calcular_perimetro())
    print (rectangulos.ang_inter())

    print (cuadrados.aristas())
    print (cuadrados.vertices())
    print (cuadrados.calculara_area())
    print (cuadrados.calcular_perimetro())
    print (cuadrados.ang_inter())

    print(f"{triangulos.calcular_area()} y {triangulos.calcular_perimetro()}")
    print (triangulos.vertices())
    print (triangulos.aristas())
    print (triangulos.ang_inter())

if __name__=="__main__":
    main()

