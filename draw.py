import networkx as nx
import matplotlib.pyplot as plt

def ler_entrada(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        lines = file.readlines()
        num_vertices = int(lines[0].strip())
        custos = {}

        for line in lines[1:]:
            i, j, k, custo = map(int, line.strip().split())
            custos[(i, j, k)] = custo

    return num_vertices, custos

def criar_grafo(num_vertices, custos):
    G = nx.DiGraph()

    # Adiciona nós
    for i in range(num_vertices):
        G.add_node(i)

    # Adiciona arestas com os pesos
    for (i, j, k), custo in custos.items():
        if custo != 0:  # Ignorar arestas com custo 0, assumindo que 0 significa nenhuma conexão
            G.add_edge(i, j, weight=custo)

    return G

def desenhar_grafo(G):
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()

def main():
    caminho_arquivo = 'entrada.txt'

    # Lendo os dados de entrada
    num_vertices, custos = ler_entrada(caminho_arquivo)

    # Criando o grafo
    G = criar_grafo(num_vertices, custos)

    # Desenhando o grafo
    desenhar_grafo(G)

if __name__ == "__main__":
    main()
