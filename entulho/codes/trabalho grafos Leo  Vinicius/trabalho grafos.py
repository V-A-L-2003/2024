import networkx as nx
import matplotlib.pyplot as plt

# Criando o grafo
G = nx.Graph()

# Adicionando vértices
vertices = ['Usuario', 'Servidor', 'DataBaseUser', 'DataBaseTreads', 'DatabaseTrackOfProcess', 
            'CPUTreads', 'TreadsTraker', 'LOG', 'ReturnToUser', 'ApiManager']
G.add_nodes_from(vertices)

# Adicionando arestas com pesos (latência em milissegundos)
arestas = [
    ('ApiManager', 'Servidor', 10), ('ApiManager', 'DataBaseUser', 15), ('ApiManager', 'DataBaseTreads', 20), 
    ('ApiManager', 'DatabaseTrackOfProcess', 25), ('ApiManager', 'CPUTreads', 30),
    ('ApiManager', 'TreadsTraker', 10), ('ApiManager', 'LOG', 35), ('ApiManager', 'ReturnToUser', 5),
    ('ApiManager', 'Usuario', 50), ('Usuario', 'Servidor', 10), ('Servidor', 'DatabaseTrackOfProcess', 15),
    ('Servidor', 'LOG', 40), ('DatabaseTrackOfProcess', 'DataBaseTreads', 10),
    ('CPUTreads', 'DataBaseTreads', 25), ('CPUTreads', 'TreadsTraker', 30),
    ('ReturnToUser', 'TreadsTraker', 20), ('DatabaseTrackOfProcess', 'TreadsTraker', 15)
]
G.add_weighted_edges_from(arestas)

# Função para exibir o grafo com pesos
def exibir_grafo_com_pesos(grafo):
    pos = nx.spring_layout(grafo)
    edge_labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', font_weight="bold", node_size=2000, font_size=10)
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels)
    plt.show()

# Função para simular balanceamento de carga
def simular_balanceamento_de_carga(grafo):
    cargas = {node: grafo.degree[node] * 10 for node in grafo.nodes}  # Exemplo: carga proporcional ao grau do nó
    print("Cargas iniciais dos nós:", cargas)
    
    # Ajustando conexões com base na carga
    sobrecarregados = [node for node, carga in cargas.items() if carga > 50]
    print("Nós sobrecarregados:", sobrecarregados)
    
    # Adicionando novas conexões para aliviar sobrecarga
    if sobrecarregados:
        for node in sobrecarregados:
            grafo.add_edge(node, 'BalanceadorCarga', weight=5)
        print("Adicionada nova conexão ao BalanceadorCarga para aliviar a carga.")

# Função para identificar nós críticos
def identificar_nos_criticos(grafo):
    critical_nodes = list(nx.articulation_points(grafo))
    print(f"Nós críticos (removê-los desconectaria o grafo): {critical_nodes}")
    return critical_nodes

# Função para simular expansão da rede
def simular_expansao_da_rede(grafo):
    novos_nos = ['CacheServer1', 'CacheServer2']
    novas_arestas = [
        ('CacheServer1', 'Servidor', 15),
        ('CacheServer2', 'Servidor', 15),
        ('CacheServer1', 'Usuario', 20),
        ('CacheServer2', 'Usuario', 20)
    ]
    grafo.add_nodes_from(novos_nos)
    grafo.add_weighted_edges_from(novas_arestas)
    print(f"Novos nós adicionados: {novos_nos}")
    print(f"Novas conexões criadas: {novas_arestas}")

# Executando funcionalidades existentes
print("Grafo inicial com pesos:")
exibir_grafo_com_pesos(G)

# Simular balanceamento de carga
print("\nSimulação de Balanceamento de Carga:")
simular_balanceamento_de_carga(G)
exibir_grafo_com_pesos(G)

# Identificar nós críticos
print("\nIdentificação de Nós Críticos:")
nos_criticos = identificar_nos_criticos(G)

# Simular expansão da rede
print("\nSimulação de Expansão da Rede:")
simular_expansao_da_rede(G)
exibir_grafo_com_pesos(G)
