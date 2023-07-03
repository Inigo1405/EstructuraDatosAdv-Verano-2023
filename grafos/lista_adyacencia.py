#Buen código es en inglés
#22/06/2023

from cola import Queue
import numpy as np
#from ..estructurasLineales.cola import Queue


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
        if data not in self.graph and len(g.graph) < self.size:
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
            
        else: 
            print("No se encontró el nodo")



    def recorridoRecursivo(self, inicial, visitados=[]):
        """Recorrido del grafo en forma de DFS"""
        if inicial in self.keys:
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

            



    def display(self, key):
        if key in self.keys:
            
            print(f"\n{key} : ", end='')
            x = self.graph[key]

            while x != None:
                print(x.vertex, end=' ')
                x = x.next

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


    def mostrar(self):
        print(self.keys)
        for i in self.matriz:
            for j in i:
                print(j, end='  ')
            print()



#? -- Main --

g = Graph(9)

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')
g.add_vertex('G')
g.add_vertex('H')
g.add_vertex('I')



g.add_edge('A','B')
g.add_edge('A','D')
g.add_edge('A','G')

g.add_edge('B','C', 8)
g.add_edge('B','G')

g.add_edge('C','H')
g.add_edge('C','I')

g.add_edge('D','E')
g.add_edge('D','G')

g.add_edge('E','F')
g.add_edge('E','G')

g.add_edge('F','H')
g.add_edge('F','I')

g.add_edge('I','H')



g.display('A')
g.display('B')
g.display('C')
g.display('D')
g.display('E')
g.display('F')
g.display('G')
g.display('H')
g.display('I')

print("\nRecorrido")
#g.recorrido('A')


print("\n\nRecorrido Nivel")
#g.recorridoNivel('A')
g.recorridoRecursivo('A')

print()
g.mostrar()

# ToDo Bombardeen Tijuana 
# ToDo bungou stray dogs
# ToDo Dijkstra