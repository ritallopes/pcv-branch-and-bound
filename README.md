# Problema do Caixeiro Viajante Quadrático: resolucao por Branch-and-bound
---

### Requisitos:

1. **Python Version:**
   - O algoritmo foi desenvolvido e testado utilizando Python na versão 3.10.12. Embora possa funcionar com outras versões 3.x, é recomendável usar especificamente versões entre 3.8.5 e 3.10.12 para garantir compatibilidade total.
   
2. **Bibliotecas Python:**
   - Certifique-se de que as seguintes bibliotecas Python estão instaladas no seu ambiente:
     - numpy
     - itertools
     - time
     - os
     - sys

     Você pode instalá-las utilizando o pip:
     ```
     pip install numpy itertools time os sys
     ```

3. **Permissões de Arquivo:**
   - Garanta que você tenha permissões adequadas para ler o arquivo de entrada e escrever no arquivo de saída especificados.

### Instruções de Execução:

1. **Argumentos de Linha de Comando:**
   - O programa espera dois argumentos de linha de comando:
     - O caminho para o arquivo de entrada que contém os dados do grafo. Este arquivo deve existir e seguir um padrão específico, incluindo informações sobre o número de vértices e os custos das arestas entre eles.
     - O caminho para o arquivo de saída onde os resultados serão escritos. Se o arquivo de saída já existir, seu conteúdo será substituído; caso contrário, um novo arquivo será criado.

2. **Exemplo de Execução:**
   - Suponha que você tenha os seguintes arquivos:
     - `arquivo_entrada.txt`: Arquivo que contém os dados do grafo.
     - `arquivo_saida.txt`: Arquivo onde os resultados serão escritos.

   - Para executar o programa com esses arquivos, você pode usar o seguinte comando no terminal:
     ```
     python qtsp_beb.py arquivo_entrada.txt arquivo_saida.txt
     ```
     Substitua `qtsp_beb.py` pelo nome do seu script Python que implementa o algoritmo BnB para resolver o QTSP.

3. **Processamento e Saída:**
   - O algoritmo processará os dados conforme especificado no arquivo de entrada e escreverá os resultados no arquivo de saída fornecido. Certifique-se de verificar o arquivo de saída após a execução para revisar os resultados do caminho ótimo encontrado e o custo associado.

---

Seguindo essas instruções passo a passo, você poderá executar o algoritmo BnB para resolver instâncias do Problema do Caixeiro Viajante Quadrático (QTSP) com os dados fornecidos no arquivo de entrada especificado.

--- 
## Programas Auxiliares:

Para facilitar a visualização do grafo presente no arquivo entrada.txt, você pode utilizar o script draw.py. Este script desenha o grafo para uma melhor compreensão visual.

Após a execução do algoritmo, você pode utilizar o script organize_FIS.py para organizar todos os resultados em um único arquivo chamado all_fis.csv. Esse arquivo consolidado facilita a análise e revisão dos resultados obtidos.