def verificar_primo(numero):
    # Verifica se o número é menor ou igual a 1
    if numero <= 1:
        return False
    # Verifica se o número é divisível por algum número de 2 até a sua metade
    for i in range(2, int(numero/2)+1):
        if numero % i == 0:
            return False
    return True

while True:
    try:
        # Solicita ao usuário que digite um número
        numero = int(input("Digite um número inteiro positivo maior que 1: "))
        # Chama a função verificar_primo e verifica se o número é primo ou não
        if verificar_primo(numero):
            print(f"{numero} é um número primo.")
            break 
        else:
            print(f"{numero} não é um número primo. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

