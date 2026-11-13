
cedulas = [100, 50, 20, 10, 5, 2]

try:

    valor = int(input('\nDigite o valor do saque em R$: '))

    if valor % 2 != 0:
        print('ERRO: O valor deve ser múltiplo de 2')

    falta_pagar = valor
    for cedula in cedulas:
        quantidade = falta_pagar // cedula 
        if quantidade > 0:
            print(f'\n{quantidade} nota(s) de R$ {cedula}')
        falta_pagar = falta_pagar % cedula

    if falta_pagar > 0:
        print(f'\nNão foi possível entregar R$ {falta_pagar} com as cédulas disponiveis.\n')
except ValueError:
    print('ERRO! Entrada inválida, digite um número inteiro')    