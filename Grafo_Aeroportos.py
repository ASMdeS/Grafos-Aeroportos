# Importando as bibliotecas que serão utilizadas no código
import networkx as nx
import matplotlib.pyplot as plt
from geopy.distance import geodesic
from FlightRadar24 import FlightRadar24API

# Inicializando o FlightRadar24API
fr_api = FlightRadar24API()

# Lista de aeroportos no mundo
world_airports = fr_api.get_airports()

# Criando um dicionário que terá como chave o código ICAO e valor coordenadas
airport_coordinates = {}

aeroportos = 0
# Preenchendo o dicionário de coordenadas com todos os aeroportos do Brasil
for airport in world_airports:
    if airport.icao[0:2] == "SB":
        aeroportos += 1 
        icao_code = airport.icao
        latitude, longitude = airport.latitude, airport.longitude
        airport_coordinates[icao_code] = (latitude, longitude)


# Criando a função que calculará a distância entre dois aeroportos
def calculate_distance(airport1, airport2):
    coord1, coord2 = airport_coordinates[airport1], airport_coordinates[airport2]
    return geodesic(coord1, coord2).kilometers


# Inicializando o dicionário que será utilizado para fazer o grafo
dicionario_grafo = {}

# Criando a variável que será usada para armazenar a maior distância entre os aeroportos mais isolados do Brasil
distancia_longinqua = 0

# Calculando a maior distância entre os aeroportos mais isolados do Brasil
for aeroporto1 in airport_coordinates:
    aeroporto_mais_proximo = float('inf')
    for aeroporto2 in airport_coordinates:
        if aeroporto1 != aeroporto2:
            distance_km = calculate_distance(aeroporto1, aeroporto2)
            if distance_km < aeroporto_mais_proximo:
                aeroporto_mais_proximo = distance_km
    if aeroporto_mais_proximo > distancia_longinqua:
        distancia_longinqua = aeroporto_mais_proximo

conexoes = 0
# Preenchendo o dicionário para que todos os aeroportos tenham um destino, porém mantendo os vértices ao mínimo
for aeroporto1 in airport_coordinates:
    dicionario_grafo[aeroporto1] = {}
    for aeroporto2 in airport_coordinates:
        if aeroporto1 != aeroporto2:
            distance_km = calculate_distance(aeroporto1, aeroporto2)
            if distance_km <= distancia_longinqua:
                dicionario_grafo[aeroporto1][aeroporto2] = int(distance_km)
                conexoes += 1

print(aeroportos)
print(conexoes)

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