# Solicita ao usuário que digite os três números inteiros separados por espaço
numeros = input("Digite três números inteiros separados por espaço: ")

# Separa os números digitados pelo usuário em uma lista
numeros = numeros.split()

# Converte os números para inteiros
numeros = [int(numero) for numero in numeros]

# Identifica o maior número entre os três
maior_numero = max(numeros)

# Imprime o maior número identificado
print(f"O maior número entre {numeros} é: {maior_numero}")
