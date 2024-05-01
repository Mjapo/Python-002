# Define a lista de valores
serie_ndvi = [0.3, -0.3, 0.2, None, 0.9, 0.8, 0.8, None, 0.2, 0.2]

# Inicializa listas 
valores_validos = []
valores_invalidos = []

# inicializando os contadores 
qtd_valores_validos = 0
qtd_valores_invalidos = 0

# Itera sobre a lista e separa os valores em listas diferentes
for valor in serie_ndvi:
    if valor is None:
        valores_invalidos.append(valor)
        qtd_valores_invalidos += 1
    else:
        valores_validos.append(valor)
        qtd_valores_validos += 1

print(f"Valores válidos: {valores_validos}")
print(f"Valores inválidos (None): {valores_invalidos}")


print(f"Quantidade de valores válidos: {qtd_valores_validos}")
print(f"Quantidade de valores inválidos (None): {qtd_valores_invalidos}")
