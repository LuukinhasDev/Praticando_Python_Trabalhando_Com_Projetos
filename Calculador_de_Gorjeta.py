def pedir_valores(mensagem):
    while True:
        texto = input(mensagem).replace(",", ".")

        try:
            valor = float(texto)
        except ValueError:
            print('Erro! Digite apenas números (sem letras ou símbolos)')
            continue

        if valor < 0:
            print('Erro! O valor não pode ser negativo.')
            continue

        return valor

conta = pedir_valores('Informe o valor da conta: R$ ')
percentual_gorjeta = pedir_valores('Informe o percentual(%) da gorjeta: ')

gorjeta = (conta * percentual_gorjeta) / 100
print('\n====CONTA DO RESTAURANTE====')
print(f'O valor da conta é: R${conta:.2f}')
print(f'A gorjeta será de: {percentual_gorjeta:.1f}%')
print(f'valor da gorjeta: R${gorjeta:.2f}')
print(f'O valor total da conta será de: R${conta + gorjeta:.2f}')  
print('=============================')  