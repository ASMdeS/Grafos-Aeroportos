import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from Grafo_Aeroportos import dicionario_grafo
from Grafo_Aeroportos import airport_coordinates
from Dijkstra import Grafo


class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Aeroportos")
        self.label_partida = ttk.Label(root, text="Partida:")
        self.label_destino = ttk.Label(root, text="Destino:")
        self.entry_partida = ttk.Entry(root)
        self.entry_destino = ttk.Entry(root)
        self.button_visualizar = ttk.Button(root, text="Visualizar", command=self.visualizar_caminho)

        #posiçao dos widgets
        self.label_partida.grid(row=0, column=0, padx=60, pady=30)
        self.label_destino.grid(row=1, column=0, padx=60, pady=30)
        self.entry_partida.grid(row=0, column=1, padx=60, pady=30)
        self.entry_destino.grid(row=1, column=1, padx=60, pady=30)
        self.button_visualizar.grid(row=2, column=0, columnspan=2, pady=30)

        #grafo para a visualização
        grafo_direcionado = nx.DiGraph(dicionario_grafo)

        #dicionário de posições dos aeroportos, no formato específico para a visulaização
        pos = {node: (coord[1], coord[0]) for node, coord in airport_coordinates.items()}

        #desenhar o grafo com todos os vertices e arestas
        nx.draw(grafo_direcionado, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue',
                font_color='black', font_size=10, edge_color='gray', arrowsize=20)

        #adicionar rótulos de peso nas arestas, representando a distancia
        edge_labels = {(i, j): dicionario_grafo[i][j] for i, j in grafo_direcionado.edges()}
        nx.draw_networkx_edge_labels(grafo_direcionado, pos, edge_labels=edge_labels)

        plt.show()

    def visualizar_caminho(self): #funçao para visualizar o caminho obtido pleo algoritmo
        aeroporto_inicial = self.entry_partida.get()
        aeroporto_final = self.entry_destino.get()

        grafo_aeroporto = Grafo(dicionario_grafo) #criando grafo 
        intervalo, caminho = grafo_aeroporto.dijkstra(aeroporto_inicial, aeroporto_final) #aplicando algoritmo de dijkstra

        #grafo para a visualização
        grafo_direcionado = nx.DiGraph(dicionario_grafo)

        #dicionário de posições dos aeroportos, no formato específico para a visulaização
        pos = {node: (coord[1], coord[0]) for node, coord in airport_coordinates.items()}

        #adicionar rótulos de peso nas arestas do caminho
        caminho_edge_labels = {(node[0], node[1]): node[2] for node in caminho}

        #visualização do caminho, se houver caminho possivel
        if caminho:
            caminho_nodes = set([node[0] for node in caminho] + [node[1] for node in caminho]) #selecao das coordenadas dos vertices
            nx.draw_networkx_nodes(grafo_direcionado, pos, nodelist=caminho_nodes, node_color='red', node_size=700) #desenhando nodes

            #adicionar rótulos dos vértices no caminho
            labels = {node: node for node in caminho_nodes}
            nx.draw_networkx_labels(grafo_direcionado, pos, labels=labels) #desenhando legendas para os vertices

            caminho_edges = [(node[0], node[1]) for node in caminho] #lista com as coordenadas das arestas
            nx.draw_networkx_edges(grafo_direcionado, pos, edgelist=caminho_edges, edge_color='red', width=2.0,
                                   arrows=True) #desenhando as arestas

            #desenhar pesos nas arestas do caminho
            nx.draw_networkx_edge_labels(grafo_direcionado, pos, edge_labels=caminho_edge_labels)

            #adicionar legenda com a distância total
            plt.text(0.5, -0.05, f"Distância Total: {intervalo} km", horizontalalignment='center',
                     verticalalignment='center', transform=plt.gca().transAxes)
            
        else:
            #se o caminho não foi encontrado, exibir mensagem de erro
            plt.text(0.5, 0.5, "Caminho não encontrado", horizontalalignment='center',
                    verticalalignment='center', transform=plt.gca().transAxes)

        #exibir o desenho
        plt.show()

#criaçao do widget
main = tk.Tk()
#criacao do app/tela
app = InterfaceGrafica(main)
main.mainloop()
