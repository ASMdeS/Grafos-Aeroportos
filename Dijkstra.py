import networkx as nx
import matplotlib.pyplot as plt
from Grafo_Aeroportos import dicionario_grafo

# Definindo o Grafo e a função Dijkstra
class Grafo:
    def __init__(self, dicionario):
        self.vertices = list(dicionario.keys())
        self.edges = dicionario

    def dijkstra(self, partida, destino):
        distancias = {aeroporto: float('inf') for aeroporto in self.vertices}
        caminhos = {aeroporto: [] for aeroporto in self.vertices}
        distancias[partida] = 0
        visitado = set()

        while len(visitado) < len(self.edges):
            aeroporto_atual = min((aeroporto for aeroporto in self.vertices if aeroporto not in visitado),
                                  key=distancias.get)
            visitado.add(aeroporto_atual)

            for vizinho, distancia in self.edges[aeroporto_atual].items():
                distancia_total = distancias[aeroporto_atual] + distancia
                if distancia_total < distancias[vizinho]:
                    distancias[vizinho] = distancia_total
                    caminhos[vizinho] = caminhos[aeroporto_atual] + [(aeroporto_atual, vizinho, distancia)]

        for aeroporto, quilometragem in distancias.items():
            if aeroporto == destino:
                return quilometragem, caminhos[aeroporto]

# Inicializando o Grafo com base no dicionário do arquivo Grafo_Aeroportos
grafo_aeroporto = Grafo(dicionario_grafo)

# Recebendo a origem
aeroporto_inicial = input("Partida: ")

# Recebendo o Destino
aeroporto_final = input("Destino: ")

# Rodando o Dijkstra com as informações
intervalo, caminho = grafo_aeroporto.dijkstra(aeroporto_inicial, aeroporto_final)

# Imprimindo a resposta
print(f"Distância: {intervalo} km. Caminho: {caminho}")

# Criando um objeto grafo direcionado a partir do dicionário
G = nx.DiGraph(dicionario_grafo)

# Desenhar o grafo
pos = nx.spring_layout(G)  # Layout para o desenho

# Adicionar rótulos de peso nas arestas apenas para aquelas no caminho
caminho_edge_labels = {(node[0], node[1]): node[2] for node in caminho}

# Destacar os vértices envolvidos no caminho encontrado pelo algoritmo de Dijkstra
if caminho:
    caminho_nodes = set([node[0] for node in caminho] + [node[1] for node in caminho])
    nx.draw_networkx_nodes(G, pos, nodelist=caminho_nodes, node_color='red', node_size=700)

    # Adicionar rótulos dos vértices apenas para aqueles no caminho
    labels = {node: node for node in caminho_nodes}
    nx.draw_networkx_labels(G, pos, labels=labels)

# Destacar as arestas envolvidas no caminho
if caminho:
    caminho_edges = [(node[0], node[1]) for node in caminho]
    nx.draw_networkx_edges(G, pos, edgelist=caminho_edges, edge_color='red', width=2.0, arrows=True)

    # Adicionar rótulos de peso nas arestas apenas para aquelas no caminho
    nx.draw_networkx_edge_labels(G, pos, edge_labels=caminho_edge_labels)

# Exibir o desenho
plt.show()
