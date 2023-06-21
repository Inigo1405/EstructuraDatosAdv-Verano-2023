import numpy as np

class Grafo:
    
    def __init__(self, n):
        self.matriz = np.array([[0 for j in range(n)] for i in range(n)])
        self.size = n

    def mostrar(self):
        for i in self.matriz:
            for j in i:
                print(j, end=' ')
            print()

    #TODO
    def insertarAdyacente(self, coords:tuple):
        x = coords[0]
        y = coords[1]

        # for i in range(self.size):
        #     for j in range(self.size):
        #         if i == x and j == y:
        #             self.matriz[i-1][j-1] = 1
        

        # for i in range(self.size):
        #     for j in range(self.size):
        #         if i == x and j == y:
        #             self.matriz[j-1][i-1] = 1

        if x == y:
            print("No se puede en la diagonal")

        else:
            self.matriz[x-1][y-1] = 1
            self.matriz[y-1][x-1] = 1
        
            


g = Grafo(8)
#g.mostrar()

coords = (1,2)
g.insertarAdyacente(coords)
print()
g.mostrar()
