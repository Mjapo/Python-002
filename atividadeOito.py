# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Solicita ao usuário que digite a letra desejada
letra = input("Digite a letra que deseja buscar na frase: ")

# Converte a frase para letras minúsculas e conta a quantidade de ocorrências da letra desejada
quantidade = frase.lower().count(letra.lower())

# Imprime a quantidade de vezes que a letra aparece na frase
print(f"A letra '{letra}' aparece {quantidade} vezes na frase.")
