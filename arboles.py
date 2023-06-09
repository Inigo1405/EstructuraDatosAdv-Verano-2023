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



    def inorden(self, arbol):
        if arbol: 
            self.preorden(arbol.izq)
            print(f'{arbol.dato}', end='→')
            self.preorden(arbol.der)



    def postorden(self, arbol):
        if arbol: 
            self.preorden(arbol.izq)
            self.preorden(arbol.der)
            print(f'{arbol.dato}', end='→')

    

    def anchura(self, arbol):
        if arbol:
            pass 



    def binarioPerfecto(self, arbol):
        pass



    def binarioLleno(self, arbol):
        pass



    def nodosHoja(self, arbol):
        if arbol:
            self.preorden(arbol.izq)
            self.preorden(arbol.der)

            if arbol.izq == None and arbol.der == None:
                print(f'{arbol.dato}', end='→')



    def peso(self, arbol):
        pass



    def nodoRaiz(self, arbol):
        if arbol:
            print(arbol.dato)
        
        return arbol.dato



    def eliminar(self, arbol, dato):
        if arbol:
            #if dato == :
            #elif dato:
            #elif dato:
            pass   




arbolito = Arbol(20)

arbolito.insertar(arbolito.raiz, 15)
arbolito.insertar(arbolito.raiz, 9)
arbolito.insertar(arbolito.raiz, 14)
arbolito.insertar(arbolito.raiz, 24)
arbolito.insertar(arbolito.raiz, 30)


print("\n\nPreorden")
arbolito.preorden(arbolito.raiz)
print("\n\nInorden")
arbolito.inorden(arbolito.raiz)
print("\n\nPostorden")
arbolito.postorden(arbolito.raiz)

print("\n\nNodo Raiz")
arbolito.nodoRaiz(arbolito.raiz)

print("\n\nNodos Hoja")
arbolito.nodosHoja(arbolito.raiz)


#print(arbolito.pesoArbol(arbolito.raiz))