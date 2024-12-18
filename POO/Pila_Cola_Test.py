from Pila import Pila
from Cola import Cola


print("Test de Pila:")
print("----------------------------")
print()
pila = Pila(2,8,9,5,3)
pila_copia = Pila(0, otro= pila)


print(f"Esta es la pila: {pila}")
print(f"Esta es la pila copia: {pila_copia}")

print(pila.valores)
print(f"El tamaño de la pila es {pila.size}")
print(pila.vacia)
#pila.vaciar()
print(pila.vacia)
pila.push(1)
pila.pop()
print(f"El primero es {pila.top()}")

print(f"La pila quedaria asi: {pila}")
print(f"Esta es la pila copia: {pila_copia}")

print("Test de Cola")
print("----------------------------")
print()

cola = Cola(2,8,9,5,3)
cola_copia = Cola(0, otro= cola)


print(f"Esta es la cola: {cola}")
print(f"Esta es la cola copia: {cola_copia}")

print(cola.valores)
print(f"El tamaño de la cola es {cola.size}")
print(cola.vacia)
#cola.vaciar()
print(cola.vacia)
cola.encolar(1)
print(f"Se elimina el {cola.desencolar()}")
print(cola.front())

print(f"La cola quedaria asi: {cola}")
print(f"Esta es la cola copia: {cola_copia}")