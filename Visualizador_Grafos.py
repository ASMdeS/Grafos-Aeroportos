import networkx as nx
import matplotlib.pyplot as plt
from Grafo_Aeroportos import dicionario_grafo

# Criando um objeto grafo direcionado a partir do dicionário
G = nx.DiGraph(dicionario_grafo)

# Desenhar o grafo
pos = nx.spring_layout(G)  # Layout para o desenho
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='gray', arrowsize=20)

# Adicionar rótulos de peso nas arestas
edge_labels = {(i, j): dicionario_grafo[i][j] for i, j in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Exibir o desenho
plt.show()
