# usando o Random para usar  a funcao random.randint - para gerar numeros aleatorios dentro da matriz 
import random
# Define a dimensão da matriz
dimensao = 10

# Cria a matriz aleatória
matriz_aleatoria = [[random.randint(0, 9) for _ in range(dimensao)] for _ in range(dimensao)]

# Imprime a matriz aleatória
for linha in matriz_aleatoria:
    print(linha)
