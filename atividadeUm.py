# criando a funcao  que calcula o fatorial de um numero inteiro nao negativo 
def calcular_fatorial(n):
    if n == 0:
        return 1, "1"
    else:
        # Chama recursivamente a função calcular_fatorial com n - 1 para calcular o fatorial do número anterior
        resultado_anterior, composicao_anterior = calcular_fatorial(n - 1)
        resultado = n * resultado_anterior
        composicao = f"{n} * {composicao_anterior}"
        return resultado, composicao

n = int(input("Digite um número inteiro entre 1 e 10: "))

if 1 <= n <= 10:
    resultado, composicao = calcular_fatorial(n)
    # imprimir o resultado calcular_fatorial com o numero inteiro digitado 
    print(f"O fatorial de {n} é {resultado} (composição: {composicao})")
else:
    # Se o número digitado não estiver entre 1 e 10, imprime uma mensagem solicitando que o usuário digite um número válido
    print("Por favor, digite um número entre 1 e 10.")
