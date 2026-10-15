def contador_de_palavras_longas(texto):

    palavras_longas = []

    for palavra in texto:
        # Limpa a palavra de pontuações 
        palavra_limpa = palavra.strip(',.!?;:')

        # Verifica se a palavra possui mais de 10 caracteres.
        if len(palavra_limpa) > 10:
            palavras_longas.append(palavra_limpa)
            
    # Retorna uma lista com as palavras longas encontradas ou uma lista vazia se nenhuma palavra longa for encontrada.            
    return palavras_longas 

texto = input('Digite um texto: ').split()
resultado = contador_de_palavras_longas(texto)

# Condição de exibição que Verifica se a função retornou uma lista vazia ou não.
if resultado:
    print(f'Palavras encontradas: {", ".join(resultado)}')
else:
    print('Nenhuma palavra longa foi encontrada no texto.')
