#Buen código es en inglés
#22/06/2023

from cola import Queue
#from ..estructurasLineales.cola import Queue


class Node:
    def __init__(self, data, weight=0):
        self.vertex = data
        self.next = None
        self.weight = weight


class Graph:
    def __init__(self, size):
        self.size = size #Tamaño del gráfico
        self.graph = {}
        self.keys = [] #Nodos enm
        # print(self.graph)
        
    def add_vertex(self, data):
        if data not in self.graph and len(g.graph) < self.size:
            self.graph[data] = []
            self.keys.append(data)
            
        else:
            print("Ya no se puede!")

        print(self.graph)


    def add_edge(self, v , w, weight=0):
        #TODO: insertar lista adyacentes

        if v in self.keys and w in self.keys:
            #*Agregar en diccionario vacío
            if self.graph[v] == []:
                self.graph[v] = Node(w, weight)


            if self.graph[w] == []:   
                self.graph[w] = Node(v, weight)
                
                
            #*Agregar diccionario existente
            if self.graph[v] != []:
                #print(self.graph[v].vertex)
                ultimo_nodo = self.graph[v]

                while ultimo_nodo.next != None:
                    ultimo_nodo = ultimo_nodo.next

                if ultimo_nodo.vertex != w:
                    ultimo_nodo.next = Node(w, weight)

            
            if self.graph[w] != []:
                ultimo_nodo = self.graph[w]

                while ultimo_nodo.next != None:
                    ultimo_nodo = ultimo_nodo.next

                if ultimo_nodo.vertex != v:
                    ultimo_nodo.next = Node(v, weight)
           
            

    def recorrido(self, inicial, visitados=list(), nodos=Queue()):
        """Recorrido del grafo en  forma de DFS"""
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



    def recorridoNivel(self, inicial, visitados=list(), nodos=list()):
        """Recorrido del grafo en  forma de BFS"""
        if inicial in self.keys:
        
            if inicial not in visitados:
                visitados.append(inicial)

            x = self.graph[inicial]
            if nodos == []:
                while x != None:
                    if x.vertex not in nodos and x.vertex not in visitados:
                        nodos.append(x.vertex)
                    x = x.next

            else:
                while x != None:
                    if x.vertex not in nodos and x.vertex not in visitados:
                        nodos.insert(0, x.vertex)
                    x = x.next

            print("\nFila: ", end='')
            print(nodos)

            print("Visitados: ", end='')
            print(visitados)

            if nodos: 
                self.recorridoNivel(nodos.pop(0), visitados, nodos)
            
        else: 
            print("No se encontró el nodo")



    def display(self, key):
        if key in self.keys:
            
            print(f"\nEl nodo {key} conecta con: ", end='')
            x = self.graph[key]

            while x != None:
                print(x.vertex, end=' ')
                x = x.next

        else:
            print("\nNo se encuentra la llave :(")

    
        

#? -- Main --

g = Graph(5)


g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)



g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 1)
g.add_edge(2, 4)



print("\nRecorrido")
g.recorrido(0)


print("\n\nRecorrido Nivel")
g.recorridoNivel(0)

#TODO Bombardeen Tijuana 
#todo bungou stray dogs
# ToDo Dijkstra