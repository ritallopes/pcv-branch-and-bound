import os
import csv
import re
import argparse

# Função para extrair os dados dos arquivos
def extrair_dados_do_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        
    nome_arquivo = os.path.basename(caminho_arquivo)
    
    vertices = re.search(r'FIS(\d+)-', nome_arquivo).group(1)
    melhor_tour = re.search(r'Melhor tour: (.+)', conteudo).group(1)
    melhor_custo = re.search(r'Melhor custo: (\d+)', conteudo).group(1)
    tempo_execucao = re.search(r'Tempo de execução: ([\d\.]+) segundos', conteudo).group(1)
    
    return [nome_arquivo, vertices, melhor_tour, melhor_custo, tempo_execucao]

# Função principal
def main(caminho_pasta, caminho_csv):
    # Lista para armazenar os dados extraídos
    dados = []

    # Percorrer todos os arquivos na pasta
    for nome_arquivo in os.listdir(caminho_pasta):
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
        if os.path.isfile(caminho_arquivo) and nome_arquivo.endswith('.txt'):
            dados.append(extrair_dados_do_arquivo(caminho_arquivo))

    # Escrever os dados em um arquivo CSV
    with open(caminho_csv, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(['Nome do Arquivo', 'Quantidade de Vértices', 'Melhor Tour', 'Melhor Custo', 'Tempo de Execução'])
        escritor_csv.writerows(dados)

    print(f"Dados extraídos e salvos em '{caminho_csv}'.")

# Configuração do argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extrair dados de arquivos de texto e salvar em um arquivo CSV.')
    parser.add_argument('pasta', type=str, help='Nome da pasta contendo os arquivos de texto.')
    parser.add_argument('csv', type=str, help='Nome do arquivo CSV de saída.')
    
    args = parser.parse_args()
    
    main(args.pasta, args.csv)
