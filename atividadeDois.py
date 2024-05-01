def fibonacci(n):
    # Inicializa os dois primeiros termos da sequência
    a, b = 0, 1
    # Lista para armazenar os termos da sequência
    sequencia = [a, b]  # Adiciona os dois primeiros termos à lista
    # Calcula os termos seguintes da sequência até alcançar n termos
    for _ in range(2, n):
        a, b = b, a + b  
        sequencia.append(b)  
    return sequencia

# Solicita ao usuário que digite o número de termos da sequência de Fibonacci a serem calculados
n = int(input("Digite o número de termos da sequência de Fibonacci a serem calculados: "))

# Calcula a sequência de Fibonacci para o número n especificado pelo usuário
resultado = fibonacci(n)

# Imprime a sequência de Fibonacci calculada
print(f"A sequência de Fibonacci para {n} termos é: {resultado}")
