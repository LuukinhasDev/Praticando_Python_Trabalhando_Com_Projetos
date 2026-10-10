# Mensagem de erro
def mensagem_erro():
    print('======================')
    print('Erro ao validar CPF!')
    print('O CPF deve conter exatamente 11 dígitos')
    print('Sem letras ou caracteres especiais. Apenas números!')
    print('======================')

while True:
    cpf = input('Digite seu CPF(apenas números): ')
    
    if len(cpf) == 11 and cpf.isdigit():
        break

    mensagem_erro()

print('CPF válido!')
