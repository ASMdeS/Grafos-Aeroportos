from Grafo_Aeroportos import dicionario_grafo

class Grafo:
    def __init__(self, dicionario):
        self.vertices = list(dicionario.keys())
        self.edges = dicionario

    def dijkstra(self, partida, destino):
        distancias = {aeroporto: float('inf') for aeroporto in self.vertices}
        caminhos = {aeroporto: [] for aeroporto in self.vertices}
        distancias[partida] = 0
        visitado = set


grafo_aeroporto = Grafo(dicionario_grafo)

grafo_aeroporto.dijkstra("SBGR", "SBRF")