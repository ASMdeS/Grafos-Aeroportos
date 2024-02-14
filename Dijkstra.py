# Importando o Grafo do arquivo Grafo_Aeroportos
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
                    caminhos[vizinho] = caminhos[aeroporto_atual] + [aeroporto_atual]

        for aeroporto, quilometragem in distancias.items():
            if aeroporto == destino:
                return quilometragem, (caminhos[aeroporto] + [aeroporto])


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
