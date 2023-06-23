#Buen código es en inglés
#22/06/2023
import threading


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
            #for i in range(2):
            #Agregar en diccionario vacío
            if self.graph[v] == []:
                self.graph[v] = Node(w)


            if self.graph[w] == []:   
                self.graph[w] = Node(v)
                
                
            #Agregar diccionario existente
            if self.graph[v] != []:
                #print(self.graph[v].vertex)
                ultimo_nodo = self.graph[v]

                while ultimo_nodo.next != None:
                    ultimo_nodo = ultimo_nodo.next

                if ultimo_nodo.vertex != w:
                    ultimo_nodo.next = Node(w)


            #Agregar diccionario existente
            if self.graph[w] != []:
                ultimo_nodo = self.graph[w]

                while ultimo_nodo.next != None:
                    ultimo_nodo = ultimo_nodo.next

                if ultimo_nodo.vertex != v:
                    ultimo_nodo.next = Node(v)


            print(self.graph)
            x = self.graph[v]

            while x != None:
                print(x.vertex)
                x = x.next
            



#? -- Main --

g = Graph(5)
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')


g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('A', 'D')




