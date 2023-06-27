#Buen código es en inglés
#22/06/2023
from cola import Queue


class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, size):
        self.size = size #Tamaño del gráfico
        self.graph = {}
        # print(self.graph)
        
    def add_vertex(self, data):
        if data not in self.graph and len(g.graph) < self.size:
            self.graph[data] = []
            
        else:
            print("Ya no se puede!")

        print(self.graph)
        return self.graph.keys()
        


    def add_edge(self, v , w):
        #TODO: insertar lista adyacentes
        keys = self.graph.keys()

        if v in keys and w in keys:
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


            #*Mostrar datos de la llave
            #print(self.graph)
            x = self.graph[v]

            while x != None:
                #print(x.vertex)
                x = x.next
            

    def recorrido(self, inicial, visitados=list(), nodos=Queue()):
        keys = self.graph.keys()
        if inicial in keys:

            if inicial not in visitados:
                visitados.append(inicial)


            x = self.graph[inicial]
            while x != None:
                if x.vertex not in nodos.datos() and x.vertex not in visitados:
                    nodos.enqueue(x.vertex)
                x = x.next

            print("\nCola:", end='')
            nodos.display()

            print("Visitados:", end='')
            print(visitados)

            self.recorrido(nodos.dequeue(), visitados, nodos)
            
        else: 
            print("No se encontró el nodo")



#? -- Main --

g = Graph(7)
# g.add_vertex('A')
# g.add_vertex('B')
# g.add_vertex('C')
# g.add_vertex('D')
# g.add_vertex('E')
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
g.add_vertex(7)

# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('A', 'D')
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(3, 6)
g.add_edge(4, 7)
g.add_edge(6, 7)
g.add_edge(5, 6)


print("\nRecorrido")
g.recorrido(1)

