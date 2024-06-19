import numpy as np
from itertools import permutations
import time
import os
import sys

def ler_entrada(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        lines = file.readlines()
        num_vertices = int(lines[0].strip())
        custos = {}

        for line in lines[1:]:
            i, j, k, custo = map(int, line.strip().split())
            custos[(i, j, k)] = custo

    return num_vertices, custos

def calcular_custo_tour(tour, custos):
    custo_total = 0
    n = len(tour)
    for i in range(n):
        custo_total += custos.get((tour[i], tour[(i+1) % n], tour[(i+2) % n]), float('inf'))
    return custo_total

def calcular_limite_inferior(tour_parcial, custos, num_vertices):
    # Esta função calcula um limite inferior para um tour parcial
    custo_total = calcular_custo_tour(tour_parcial, custos)
    vertices_restantes = set(range(num_vertices)) - set(tour_parcial)

    if not vertices_restantes:
        return custo_total

    # Adiciona um custo mínimo aproximado para as arestas faltantes
    custo_estimado = 0
    for i in vertices_restantes:
        menor_custo = min(custos.get((tour_parcial[-1], i, j), float('inf')) for j in vertices_restantes)
        custo_estimado += menor_custo

    return custo_total + custo_estimado

def branch_and_bound(num_vertices, custos):
    melhor_tour = None
    melhor_custo = float('inf')
    pilha = [([i], 0) for i in range(num_vertices)]

    while pilha:
        tour_parcial, custo_parcial = pilha.pop()

        if len(tour_parcial) == num_vertices:
            custo_total = calcular_custo_tour(tour_parcial, custos)
            if custo_total < melhor_custo:
                melhor_custo = custo_total
                melhor_tour = tour_parcial
        else:
            limite_inferior = calcular_limite_inferior(tour_parcial, custos, num_vertices)
            if limite_inferior < melhor_custo:
                for i in range(num_vertices):
                    if i not in tour_parcial:
                        novo_tour_parcial = tour_parcial + [i]
                        novo_custo_parcial = calcular_custo_tour(novo_tour_parcial, custos)
                        pilha.append((novo_tour_parcial, novo_custo_parcial))

    return melhor_tour, melhor_custo


def main():
    if len(sys.argv)!= 3:
        print("Uso: python/python3 grafos.py <entrada.txt> <saida.txt>")
        sys.exit(1)

    caminho_entrada = sys.argv[1]
    caminho_saida = sys.argv[2]
    print(f'Processando o arquivo {caminho_entrada}')
    # Lendo os dados de entrada
    num_vertices, custos = ler_entrada(caminho_entrada)

    # Resolvendo o QTSP usando branch-and-bound
    inicio = time.time()
    melhor_tour, melhor_custo = branch_and_bound(num_vertices, custos)
    fim = time.time()
    print(f'Melhor tour: {melhor_tour}')
    print(f'Melhor custo: {melhor_custo}')
    print(f'Tempo de execução: {fim - inicio} segundos')
    print(f'As informações estão armazenados no arquivo {caminho_saida}')
    with open(caminho_saida, 'w') as arquivo_saida:
      arquivo_saida.write(f'Processando arquivo: {caminho_entrada}\n')
      arquivo_saida.write(f'Melhor tour: {melhor_tour}\n')
      arquivo_saida.write(f'Melhor custo: {melhor_custo}\n')
      arquivo_saida.write(f'Tempo de execução: {fim - inicio} segundos\n')

if __name__ == "__main__":
    main()