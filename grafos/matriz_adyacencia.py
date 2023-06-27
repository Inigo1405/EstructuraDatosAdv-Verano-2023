import numpy as np

class Grafo:
    
    def __init__(self, n):
        self.matriz = np.array([[0 for j in range(n)] for i in range(n)])
        self.size = n

    def mostrar(self):
        for i in self.matriz:
            for j in i:
                print(j, end='  ')
            print()

    #TODO
    def insertarAdyacente(self, coords:tuple):
        x = coords[0]
        y = coords[1]

        if x > 0 and y > 0:
            self.matriz[x-1][y-1] = 1
            self.matriz[y-1][x-1] = 1

        else:
            print("No se puede añadir en esta ubicación")

            
    def eliminarAdyacente(self, coords:tuple):
        x = coords[0]
        y = coords[1]

        if x > 0 and y > 0 and self.matriz[x-1][y-1] == 1 and self.matriz[y-1][x-1] == 1:
            self.matriz[x-1][y-1] = 0
            self.matriz[y-1][x-1] = 0

        else:
            print("No se puede eliminar en esta ubicación")

g = Grafo(8)
#g.mostrar()

g.insertarAdyacente((1,2))
g.insertarAdyacente((1,3))

g.insertarAdyacente((2,3))
g.insertarAdyacente((2,4))
g.insertarAdyacente((2,5))

g.insertarAdyacente((3,5))
g.insertarAdyacente((3,8))

g.insertarAdyacente((4,5))

g.insertarAdyacente((5,6))

g.insertarAdyacente((7,8))



g.mostrar()
print()

g.eliminarAdyacente((8,7))
g.mostrar()