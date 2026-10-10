# Mensagem de erro
def mensagem_erro():
    print('======================')
    print('Erro ao validar CPF!')
    print('O CPF deve conter exatamente 11 dígitos')
    print('Sem letras ou caracteres especiais. Apenas números!')
    print('======================')

while True:
    cpf = input('Digite seu CPF(anpenas números): ')
    contador = 0
    caractere_nao_numerico = False

    for digito in cpf:
        contador += 1

        if not digito.isdigit():
            caractere_nao_numerico = True

    if contador == 11 and not caractere_nao_numerico:
        break

    mensagem_erro()

print('CPF válido!')


