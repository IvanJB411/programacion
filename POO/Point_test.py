#Prueba point
from point import Point
if __name__ == "__main__":

    p1 = Point(3, 5)
    p2 = Point(4, 2)
    """print(p1)
    print("-Quiero que se inviertan x e y")
    print(p1.invertir_coordenadas())
    print(p1)
    print("-Ahora la x va a ser 0")
    p1.valor_x = 0
    print(p1)"""

    p3 = p1 + p2

    print(p3)
    print(f"La reta es {p1 - p2}")