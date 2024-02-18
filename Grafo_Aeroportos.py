#importando Geopy para calcular a distância entre aeroportos e o FlightRadar24 para pegar as coordenadas dos aeroportos
from geopy.distance import geodesic
from FlightRadar24 import FlightRadar24API

#inicializando a API
fr_api = FlightRadar24API()

#lista de aeroportos no mundo
world_airports = fr_api.get_airports()

#dicionario com chave o código ICAO e valor coordenadas
airport_coordinates = {}

#preenchendo o dicionario 
for airport in world_airports:
    if airport.icao[0:2] == "SB":
        icao_code = airport.icao
        latitude, longitude = airport.latitude, airport.longitude
        airport_coordinates[icao_code] = (latitude, longitude)


#calculo da distância entre dois aeroportos
def calculate_distance(airport1, airport2):
    coord1, coord2 = airport_coordinates[airport1], airport_coordinates[airport2]
    return geodesic(coord1, coord2).kilometers


#dicionário utilizado para fazer o grafo
dicionario_grafo = {}

#armazenar a maior distância entre dois aeroportos
distancia_longinqua = 0

#calcular a maior distancia
for aeroporto1 in airport_coordinates:
    aeroporto_mais_proximo = float('inf')
    for aeroporto2 in airport_coordinates:
        if aeroporto1 != aeroporto2:
            distance_km = calculate_distance(aeroporto1, aeroporto2)
            if distance_km < aeroporto_mais_proximo:
                aeroporto_mais_proximo = distance_km
    if aeroporto_mais_proximo > distancia_longinqua:
        distancia_longinqua = aeroporto_mais_proximo


# Preenchendo o dicionário do grafo
for aeroporto1 in airport_coordinates:
    dicionario_grafo[aeroporto1] = {}
    for aeroporto2 in airport_coordinates:
        if aeroporto1 != aeroporto2:
            distance_km = calculate_distance(aeroporto1, aeroporto2)
            if distance_km <= distancia_longinqua:
                dicionario_grafo[aeroporto1][aeroporto2] = int(distance_km)               
