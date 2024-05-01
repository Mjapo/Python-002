# Função para calcular a frequência relativa de vogais em um texto
def frequencia_vogais(texto):
    # Converte o texto para letras minúsculas
    texto = texto.lower()
    # Conta o total de letras no texto
    total_letras = len(texto)
    # Inicializa um dicionário para contar o número de vezes que cada vogal aparece
    contagem_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Conta o número de vezes que cada vogal aparece no texto
    for letra in texto:
        if letra in contagem_vogais:
            contagem_vogais[letra] += 1
    
    # Calcula a frequência relativa de cada vogal
    frequencia_vogais = {vogal: contagem/total_letras for vogal, contagem in contagem_vogais.items()}
    
    return frequencia_vogais

# Solicita ao usuário que digite um texto
texto = input("Digite um texto: ")

# Calcula a frequência relativa de vogais no texto
resultado = frequencia_vogais(texto)

# Imprime a frequência relativa de cada vogal
for vogal, frequencia in resultado.items():
    print(f"A vogal '{vogal}' aparece com frequência relativa de {frequencia:.2f}")
