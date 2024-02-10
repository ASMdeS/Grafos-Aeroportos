# Importando as bibliotecas que serão utilizadas no código
from geopy.distance import geodesic
from FlightRadar24 import FlightRadar24API

# Inicializando o FlightRadar24API
fr_api = FlightRadar24API()

# Lista de aeroportos no mundo
world_airports = fr_api.get_airports()

# Criando um dicionário que terá como chave o código ICAO e valor coordenadas
airport_coordinates = {}

# Lista de códigos ICAO de aeroportos brasileiros
lista_icao = ['SBSR', 'SBSL', 'SBBZ', 'SBMA', 'SBEG', 'SBBR', 'SBPK', 'SBJP', 'SBNF', 'SBMQ', 'SBSG', 'SBCV', 'SBPA',
              'SBRJ', 'SBAT', 'SBCB', 'SBMD', 'SBCR', 'SBGO', 'SBMY', 'SBJH', 'SBUR', 'SBCZ', 'SBPS', 'SBDB', 'SBRF',
              'SBCP', 'SBLO', 'SBJV', 'SBMO', 'SBJA', 'SBJU', 'SBSP', 'SBVC', 'SBKG', 'SBCG', 'SBSJ', 'SBBI', 'SBPP',
              'SBBV', 'SBKP', 'SBAC', 'SBPG', 'SBBG', 'SBCM', 'SBIZ', 'SBAN', 'SBJR', 'SBGV', 'SBRD', 'SBTS', 'SBSO',
              'SBUL', 'SBFI', 'SBVG', 'SBBH', 'SBCY', 'SBNM', 'SBPF', 'SBVT', 'SBBE', 'SBTG', 'SBTF', 'SBPJ', 'SBFL',
              'SBJI', 'SBUG', 'SBTD', 'SBMN', 'SBJE', 'SBJF', 'SBJD', 'SBTT', 'SBCF', 'SBSM', 'SBSI', 'SBHT', 'SBZM',
              'SBIH', 'SBRB', 'SBAU', 'SBAX', 'SBTC', 'SBPB', 'SBMK', 'SBCT', 'SBPV', 'SBST', 'SBBP', 'SBLJ', 'SBME',
              'SBFZ', 'SBPL', 'SBUA', 'SBMT', 'SBPO', 'SBLE', 'SBGL', 'SBCN', 'SBAE', 'SBIP', 'SBBW', 'SBCJ', 'SBCA',
              'SBMG', 'SBSV', 'SBDO', 'SBFN', 'SBRP', 'SBGR', 'SBTU', 'SBSN', 'SBCX', 'SBTE', 'SBCH', 'SBDN', 'SBSC',
              'SBTB', 'SBUF', 'SBML', 'SBAQ', 'SBAR', 'SBIL', 'SBMS', 'SBVH']

# Preenchendo o dicionário
for airport in world_airports:
    icao_code = airport.icao
    latitude, longitude = airport.latitude, airport.longitude
    airport_coordinates[icao_code] = (latitude, longitude)


# Criando a função que calculará a distância entre dois aeroportos
def calculate_distance(airport1, airport2):
    coord1, coord2 = airport_coordinates[airport1], airport_coordinates[airport2]
    return geodesic(coord1, coord2).kilometers


# Inicializando o dicionário que será utilizado para fazer o grafo
dicionario_grafo = {}

# Preenchendo o dicionário
for aeroporto1 in lista_icao:
    dicionario_grafo[aeroporto1] = {}
    for aeroporto2 in lista_icao:
        if aeroporto1 != aeroporto2:
            distance_km = calculate_distance(aeroporto1, aeroporto2)
            # print(f"Distance between {aeroporto1} and {aeroporto2}: {distance_km:.2f} km")
            dicionario_grafo[aeroporto1][aeroporto2] = int(distance_km)
