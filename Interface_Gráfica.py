import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from Grafo_Aeroportos import dicionario_grafo
from Dijkstra import Grafo

class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Aeroportos")

        # Criando os widgets
        self.label_partida = ttk.Label(root, text="Partida:")
        self.label_destino = ttk.Label(root, text="Destino:")
        self.entry_partida = ttk.Entry(root)
        self.entry_destino = ttk.Entry(root)
        self.button_visualizar = ttk.Button(root, text="Visualizar", command=self.visualizar_grafo)

        # Organizando os widgets na janela
        self.label_partida.grid(row=0, column=0, padx=10, pady=5)
        self.label_destino.grid(row=1, column=0, padx=10, pady=5)
        self.entry_partida.grid(row=0, column=1, padx=10, pady=5)
        self.entry_destino.grid(row=1, column=1, padx=10, pady=5)
        self.button_visualizar.grid(row=2, column=0, columnspan=2, pady=10)

    def visualizar_grafo(self):
        aeroporto_inicial = self.entry_partida.get()
        aeroporto_final = self.entry_destino.get()

        grafo_aeroporto = Grafo(dicionario_grafo)
        intervalo, caminho = grafo_aeroporto.dijkstra(aeroporto_inicial, aeroporto_final)

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

            # Adicionar legenda com a distância total
            plt.text(0.5, -0.05, f"Distância Total: {intervalo} km", horizontalalignment='center',
                    verticalalignment='center', transform=plt.gca().transAxes)

        # Exibir o desenho
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()
