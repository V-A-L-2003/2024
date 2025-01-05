import networkx as nx
import matplotlib.pyplot as plt

# Criando o grafo
G = nx.Graph()

# Adicionando vértices
vertices = ['Usuario', 'Servidor', 'DataBaseUser', 'DataBaseTreads', 'DatabaseTrackOfProcess', 
            'CPUTreads', 'TreadsTraker', 'LOG', 'ReturnToUser', 'ApiManager']
G.add_nodes_from(vertices)

# Adicionando arestas entre os vértices com pesos implícitos iguais
arestas = [
    ('ApiManager', 'Servidor'), ('ApiManager', 'DataBaseUser'), ('ApiManager', 'DataBaseTreads'), 
    ('ApiManager', 'DatabaseTrackOfProcess'), ('ApiManager', 'CPUTreads'),
    ('ApiManager', 'TreadsTraker'), ('ApiManager', 'LOG'), ('ApiManager', 'ReturnToUser'),
    ('ApiManager', 'Usuario'), ('Usuario', 'Servidor'),('Servidor', 'DatabaseTrackOfProcess'),
    ('Servidor', 'LOG'),('DatabaseTrackOfProcess', 'DataBaseTreads'),('CPUTreads', 'DataBaseTreads'),
    ('CPUTreads', 'TreadsTraker'),('ReturnToUser', 'TreadsTraker'),('DatabaseTrackOfProcess', 'TreadsTraker'),
]
G.add_edges_from(arestas)

# Função para exibir o grafo
def exibir_grafo(grafo):
    pos = nx.spring_layout(grafo)  # Posição dos nós no gráfico

    # Desenhando o grafo
    plt.figure(figsize=(8, 6))  # Definindo o tamanho da figura
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', font_weight="bold", 
            edge_color='gray', node_size=2000, font_size=10)
    plt.title("Exibição do Grafo")
    plt.show()

# Exibindo o grafo
exibir_grafo(G)
