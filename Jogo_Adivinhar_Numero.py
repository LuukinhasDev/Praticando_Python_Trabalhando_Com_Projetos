import random

num_secreto = random.randint(1, 100)

while True:
    palpite = int(input('Tente adivinhar o número (1-100): '))

    if palpite > num_secreto:
        print('Tente um valor mais baixo')
        

    elif palpite < num_secreto: 
        print('Tente um valor mais alto')
        

    else:
        break

print()
print('=-'*25)
print(f'Parabéns! você descobriu o número secreto {num_secreto}')
print('=-'*25)
print()
    