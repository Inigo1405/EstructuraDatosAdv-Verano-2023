import matplotlib.pyplot as plt
import networkx as nx

# Crear un grafo
G = nx.Graph()

# Agregar nodos
G.add_nodes_from([1, 2, 3, 4, 5])

# Agregar aristas
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (4, 5)])

# Graficar el grafo
pos = nx.spring_layout(G)  # Posiciones de los nodos
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()
