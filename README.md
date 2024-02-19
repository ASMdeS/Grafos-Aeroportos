Sistema de Visualização e Análise de Aeroportos

Este sistema consiste em três componentes principais que juntos fornecem funcionalidades para visualizar, analisar e encontrar rotas entre aeroportos:
Componentes:
1. Grafo_Aeroportos.py

    Este script cria um grafo de aeroportos com base em informações de localização geográfica e distâncias entre eles.
    Utiliza a API do FlightRadar24 para obter informações sobre aeroportos em todo o mundo.
    Implementa funções para calcular a distância entre aeroportos e preencher um dicionário que representa o grafo.

2. Dijkstra.py

    Contém uma implementação do algoritmo de Dijkstra para encontrar o caminho mais curto em um grafo ponderado.
    Define a classe Grafo com o método dijkstra(partida, destino) para calcular o caminho mais curto entre dois aeroportos no grafo.

3. Interface_Gráfica.py

    Implementa uma interface gráfica simples usando Tkinter para visualizar o grafo de aeroportos e encontrar rotas entre eles.
    Utiliza a biblioteca networkx para representar graficamente o grafo de aeroportos e a biblioteca matplotlib para desenhar o grafo e destacar caminhos.

Funcionamento do Sistema:

    O script Grafo_Aeroportos.py cria um grafo de aeroportos com base em dados de localização e distância.
    Dijkstra.py fornece um algoritmo eficiente para encontrar o caminho mais curto entre aeroportos no grafo.
    Interface_Gráfica.py oferece uma interface intuitiva para os usuários inserirem aeroportos de partida e destino, e visualizarem os caminhos mais curtos entre eles.

Execução:

    Certifique-se de ter as bibliotecas necessárias instaladas em seu ambiente Python: tkinter, networkx, matplotlib, geopy, e FlightRadar24 (se for utilizar).
    Execute o script Interface_Gráfica.py para iniciar a interface gráfica.
    Insira os códigos ICAO dos aeroportos de partida e destino nos campos apropriados.
    Clique no botão "Visualizar" para encontrar e destacar o caminho mais curto entre os aeroportos inseridos.

Autor:

Este sistema foi desenvolvido por Arthur Santos Marinho de Souza e Felipe de Souza Santos.

Para sugestões, dúvidas ou contribuições, entre em contato via asms@cin.ufpe.br ou fss9@cin.ufpe.br.
