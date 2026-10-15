def contador_de_vogais(texto):    
    vogais = 'aeiouAEIOUáàâãéêíóôõúÁÀÂÃÉÊÍÓÔÕÚ'
    Vogais_no_texto = 0


    for letra in texto:
        if letra in vogais:
            Vogais_no_texto += 1
            
    return Vogais_no_texto

texto = input('Digite uma frase ou texto: ')
print(f'O texto digitado contém {contador_de_vogais(texto)} vogais')