# Loop externo de 1 a 10 para o multiplicador
for i in range(1, 11):
    # Loop interno de 1 a 10 para o multiplicando
    for j in range(1, 11):
        # Calcula o resultado da multiplicação
        resultado = i * j
        # Imprime a operação e o resultado formatados
        print(f"{i} x {j} = {resultado}")
    # Adiciona uma linha em branco após cada tabela de multiplicação
    print()
