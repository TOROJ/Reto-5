# Reto 5  _Juan_ _Toro_
En este reto vamos a usar los paquetes y los modulos para una mayor organización del código, usamos from e import, para llamar a los diferentes modulos desde main.

## Estuctura de paquetes y modulos
La estructura para este reto 5 seria el siguiente:

```
Reto 5!
└── Shape_individual/  # Paquete con modulos individuales
    ├── __init__.py
    ├── class_point.py  # Contiene la clase punto
    ├── class_linea.py  # Contiene la clase linea
    ├── class_cuadrado.py  # Contiene la clase cuadrado
    ├── clase_rectangulo.py  # Contiene la clase rectangulo
    └── class_triangulo.py # Contiene la clase triangulo
└── Shape/  #Paquete con un solo modulo individual
    ├── __init__.py  
    └── total.py 
├── main 1.py  # Archivo que contiene código de prueba individual
├── main 2.py  # Archivo que contiene código de prueba de un modulo
```
## Explicación:
El paquete total esta dividido en dos paquetes, los cuales dividi en el que estara **un modulo** que es igual a todo el código en general... como si fuera normal
y el otro, que se encuentran otra sub división de la división de la... (y así) de los cuales se dividieron en modulos por cada clase, algo curioso es que es obligatorio poner en cada 
paquete "**__init__.py**" peeero,  es necesario tambien poner un main, del cual este retomara los datos propuestos y se llamaran con el import (_¿muy confuso?_ ) 
para darse una idea:
```python
def main():
    from Shape_individual.class_rectangulo import Rectangulo
    from Shape_individual.class_cuadrado import Cuadrado
    from Shape_individual.class_triangulo import Triangulo
```
Este es como un guia para la consola, que dara como resultado el lugar especifico que necesitamos de tooooda el paquete.
lastimosamente... (_ja_) no supe como agrupar ambos en un solo main así que hice dos main.... ¿y pues sera contradictorio que hallán dos main?  _no lo sé_
el punto, use dos main, el primero me dara el resultado que quiero poniendo los datos requeridos y el segundo... igual. con la diferencía de que en ambos aunque use import y from, 
cada uno llamo modulos totalmente diferentes(_casí_).

ya para acabar...
## concluciones y demás:
principalmente el reto se basa en tener un orden y poderlo usar gracias a los imports en los ejercicios ya vistos anteriormente, me parecio bastante sencillo pero muy eficaz a la hora de organizar
siendo sincero aquel dia de aquel año, me parecio que poner toda la informacion de un rectangulo en un modulo fue abrumador, ver clase por clase y no saber el error, mirar y ver que faltaban
algunas cositas, este tema de paquetes lo veo util para mejorar en este aspecto, lo unico seria saber usar los imports.
(algo curioso... al usar los main se crea un nuevo modulo que se llama "__pyache__"... pero esto sera tema para otro día.)
Hasta el Proximo Reto: 
bai (bye)
