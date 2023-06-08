from nodoArbol import Nodo

class Arbol():
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def insertar(self, arbol, dato):
        
        # Agregar al inicio
        if arbol is None:
           return Nodo(dato)

        # Agregar a la izq del arbol el dato menor
        elif dato < arbol.dato:
            arbol.izq = self.insertar(arbol.izq, dato)


        # Agregar a la der del arbol el dato mayor
        elif dato > arbol.dato:
            arbol.der = self.insertar(arbol.der, dato)
            
        return arbol


    def preorden(self, arbol):
        if arbol: 
            print(f'{arbol.dato}', end='→')
            self.preorden(arbol.izq)
            self.preorden(arbol.der)



arbolito = Arbol(20)
print(arbolito.raiz.dato)
arbolito.insertar(arbolito.raiz, 15)
arbolito.insertar(arbolito.raiz, 9)
arbolito.insertar(arbolito.raiz, 14)
arbolito.preorden(arbolito.raiz)
print(arbolito.raiz.dato)
