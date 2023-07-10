#Buen código es en inglés
#22/06/2023

import time
from cola import Queue
import numpy as np


class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, size):
        self.size = size #Tamaño del gráfico
        self.graph = {} #Diccionario con el grafo
        self.keys = [] #Nodos enm
        self.matriz = np.array([[0 for j in range(size)] for i in range(size)])
        # print(self.graph)
        
    
    def add_vertex(self, data):
        """Agrega los nodos al grafo"""
        if data not in self.graph and len(self.graph) < self.size:
            self.graph[data] = []
            self.keys.append(data)
            
        else:
            print("Ya no se puede!")

        print(self.graph)



    def add_edge(self, v , w, peso=1):
        #TODO: insertar lista adyacentes

        if v in self.keys and w in self.keys:
            #*Agregar en diccionario vacío
            if self.graph[v] == []:
                self.graph[v] = Node(w)


            if self.graph[w] == []:   
                self.graph[w] = Node(v)
                
                
            #*Agregar diccionario existente
            if self.graph[v] != []:
                #print(self.graph[v].vertex)
                ultimo_nodo = self.graph[v]

                while ultimo_nodo.next != None:
                    ultimo_nodo = ultimo_nodo.next

                if ultimo_nodo.vertex != w:
                    ultimo_nodo.next = Node(w)

            
            if self.graph[w] != []:
                ultimo_nodo = self.graph[w]

                while ultimo_nodo.next != None:
                    ultimo_nodo = ultimo_nodo.next

                if ultimo_nodo.vertex != v:
                    ultimo_nodo.next = Node(v)
        
            self.matrizPeso(v, w, peso)



    def recorrido(self, inicial, visitados=list(), nodos=Queue()):
        """Recorrido del grafo en forma de BFS"""
        if inicial in self.keys:

            if inicial not in visitados:
                visitados.append(inicial)

            x = self.graph[inicial]
            while x != None:
                if x.vertex not in nodos.datos() and x.vertex not in visitados:
                    nodos.enqueue(x.vertex)
                x = x.next

            print("\nCola: ", end='')
            nodos.display()

            print("Visitados: ", end='')
            print(visitados)

            self.recorrido(nodos.dequeue(), visitados, nodos)
            return visitados



    def recorridoRecursivo(self, inicial, visitados=[]):
        """Recorrido del grafo en forma de DFS"""
        if inicial in self.keys:
            if inicial not in visitados:
                visitados.append(inicial)
            print(visitados) 

            x = self.graph[inicial]
            if x.vertex not in visitados:
                self.recorridoRecursivo(x.vertex, visitados)
            
            else:
                while x != None:
                    if x.vertex not in visitados:
                        self.recorridoRecursivo(x.vertex, visitados)
                    x = x.next

            return visitados

            
            


    def display(self, key):
        if key in self.keys:
            print(f"\n{key} : ", end='')
            if self.graph[key] != []: 
                x = self.graph[key]

                while x != None:
                    print(x.vertex, end=' ')
                    x = x.next

            print()

        else:
            print("\nNo se encuentra la llave :(")



    def matrizPeso(self, v, w, peso):
        x = self.keys.index(v)
        y = self.keys.index(w)

        if x >= 0 and y >= 0:
            self.matriz[x][y] = peso
            self.matriz[y][x] = peso

        else:
            print("No se puede añadir en esta ubicación")



    def displayMatrix(self):
        for i in self.keys:
            print(" ", i, end='  ')
        
        max_len = len(str(np.max(self.matriz)))
        
        for row in self.matriz:
            print()
            for num in row:
                print("{:>{}}".format(num, max_len), end=' ')



    def dijkstra(self, inicio, fin, visitados=[], peso=0, visitadosPos=[]):
        """Recorrido de tipo dijkstra que trabaja con pesos en las conexiones."""
        if inicio in self.keys and fin in self.keys:
            
            visitados.append(inicio)
            visitadosPos.append(self.keys.index(inicio))

            print()
            print(visitados)
            print("Peso: ", peso)

            if inicio == fin:
                return

            row = self.keys.index(inicio)
            print(self.matriz[row]) 

            x = 0
            for i in range(self.size):
                if x == 0:
                    if i not in visitadosPos:
                        x = self.matriz[row][i]
                        pos = i
                    
                
                elif self.matriz[row][i] < x and self.matriz[row][i] != 0:
                    if self.keys[pos] not in visitados and i not in visitadosPos:
                        x = self.matriz[row][i]
                        pos = i
                
            
            print("Pos: ", pos)
            print("Min: ", x)
            print("Letra: ", self.keys[pos])
            
            #time.sleep(2)
            self.dijkstra(self.keys[pos], fin, visitados, peso + x, visitadosPos)

            return visitados, peso
            


def menu():
    # opc = int(input("Ingresa una opción"))
    print("1. Conexiones de los nodos")
    print("2. Recorrido BFS")
    print("3. Recorrido DFS")
    print("4. Mostrar matriz de pesos")
    print("5. Recorrido Dijkstra")


            

#? -- Main --

# g = Graph(9)
# # g = Graph(6)

# g.add_vertex('A')
# g.add_vertex('B')
# g.add_vertex('C')
# g.add_vertex('D')
# g.add_vertex('E')
# g.add_vertex('F')
# g.add_vertex('G')
# g.add_vertex('H')
# g.add_vertex('I')



# g.add_edge('A','B', 3)
# g.add_edge('A','D', 1)
# g.add_edge('A','G', 1)

# g.add_edge('B','C', 8)
# g.add_edge('B','G', 6)

# g.add_edge('C','H', 7)
# g.add_edge('C','I', 1)

# g.add_edge('D','E', 10)
# g.add_edge('D','G', 3)

# g.add_edge('E','F', 2)
# g.add_edge('E','G', 9)

# g.add_edge('F','H', 5)
# g.add_edge('F','I', 8)

# g.add_edge('I','H', 6)


# # g.add_edge('A', 'B', 4)
# # g.add_edge('A', 'C', 2)
# # g.add_edge('B', 'C', 1)
# # g.add_edge('B', 'D', 5)
# # g.add_edge('C', 'D', 8)
# # g.add_edge('C', 'E', 10)
# # g.add_edge('D', 'E', 2)
# # g.add_edge('D', 'F', 6)
# # g.add_edge('E', 'F', 2)



# for i in g.keys:
#     g.display(i)
    


# print("\nRecorrido")
# g.recorrido('A')


# print("\n\nRecorrido Nivel")
# g.recorridoRecursivo('A')

# print()
# g.displayMatrix()


# print()
# print()
# print()

# print("Recorrido Dijkstra")
# g.dijkstra('A', 'E')

# ToDo Bombardeen Tijuana 
# ToDo bungou stray dogs


#* GUI en python => Canvas, PyQt5
# Canvas, para grafos personalizados 
# Una estructura con los nombres de los nods: [A,B,C, ...] , [1,2,2, ...]


