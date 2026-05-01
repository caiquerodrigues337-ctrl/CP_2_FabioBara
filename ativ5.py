# Crie um programa que receba um texto do usuário e 
# conte quantas vezes cada palavra aparece, 
# armazenando em um dicionário 
# (palavra como chave, contagem como valor).
# Converta tudo para minúsculo antes de contar. 
# Ao final, exiba as palavras ordenadas pela frequência 
# (da mais frequente para a menos frequente) e 
# destaque a palavra mais usada.

texto = input("Digite um texto ou frase: ").lower()
palavras = texto.split()

contagem = {}

for palavra in palavras:
    palavra = palavra.strip(",.!?()")
    
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

palavras_ordenadas = sorted(contagem.items(), key=lambda item: item[1], reverse=True)


print("\n--- Frequência de Palavras ---")
if palavras_ordenadas:
    
    mais_comum, qtd = palavras_ordenadas[0]
    
    for palavra, frequencia in palavras_ordenadas:
        print(f"{palavra}: {frequencia}x")
    
    print("-" * 30)
    print(f"DESTAQUE: A palavra mais usada foi '{mais_comum}' ({qtd} vezes).")
else:
    print("Nenhuma palavra encontrada.")