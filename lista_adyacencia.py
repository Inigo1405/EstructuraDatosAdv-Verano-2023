#Buen código es en inglés

class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, size):
        self.size = size #Tamaño del grafi
        self.graph = {}
        # print(self.graph)
        
    def add_vertex(self, data):
        if data not in self.graph and len(g.graph) < self.size:
            self.graph[data] = []
            
        else:
            print("Ya no se puede!")

        print(self.graph)
        

    def add_edge(self, v , w):
        #TODO: instertar lista adyacencia
        keys = self.graph.keys()

        if v in keys and w in keys:

            if self.graph[v] == []:
                self.graph[v] = Node(w)
                self.graph[w] = Node(v)
            
            else:
                self.graph[v].next = Node(w)
                self.graph[w].next = Node(v)
                
            print(self.graph)

#? -- Main --

g = Graph(5)
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')

g.add_edge('A', 'B')

