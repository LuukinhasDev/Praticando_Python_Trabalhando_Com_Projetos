import random

print(''' 

░░█ █▀█ █▀▀ █▀█   █▀▄ █▀█   █▄░█ █░█ █▀▄▀█ █▀▀ █▀█ █▀█   █▀ █▀▀ █▀▀ █▀█ █▀▀ ▀█▀ █▀█
█▄█ █▄█ █▄█ █▄█   █▄▀ █▄█   █░▀█ █▄█ █░▀░█ ██▄ █▀▄ █▄█   ▄█ ██▄ █▄▄ █▀▄ ██▄ ░█░ █▄█
''')

num_secreto = random.randint(1, 100)
tentativas = 1

while True:
    print()
    print('=='*22)
    texto = input('Adivinhe o número secreto entre (1-100): ')

    try:
        palpite = int(texto)

    except ValueError:
        print('ERRO! Digite apenas números inteiros, sem vírgulas, letras ou símbolos.')
        continue
    
    if (palpite < 1) or (palpite > 100):
        print('ERRO! digite um valor entre 1 e 100.')
        
    else:    
        
        if palpite > num_secreto:
            print('\nTente chutar um valor mais baixo')
            
        elif palpite < num_secreto: 
            print('\nTente chutar um valor mais alto')
            
        else:
            break
    
        tentativas += 1


palavra_tentativa = 'tentativa' if tentativas == 1 else 'tentativas'
print()
print('''
==================== Ｐａｒａｂｅｎｓ！====================
''')
print(f'Você descobriu o número secreto {num_secreto} em {tentativas} {palavra_tentativa}')
print('=='*30)
print()
    