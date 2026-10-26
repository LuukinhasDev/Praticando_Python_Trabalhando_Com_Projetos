# Mensagem de erro
def mensagem_erro(texto):
    print()
    print('='*50)
    print(texto)
    print('='*50)

def calcular_digito(digitos, peso):
    soma = 0
    cont = peso
    for num in digitos:
        soma += int(num) * cont
        cont-=1

    if soma % 11 < 2:  
        digito_esperado = 0
    else:
        digito_esperado = 11 - (soma % 11)
    return digito_esperado

while True:
    cpf = input('\nDigite seu CPF(apenas números): ')
    
    if (len(cpf) != 11) or (not cpf.isdigit()):
        mensagem_erro('Erro de formato do CPF!\nO CPF deve ter exatamente 11 dígitos, apenas números.')
        continue

    if len(set(cpf)) == 1:
        mensagem_erro('Erro de repetição! o CPF não pode ter 11 dígitos iguais!')
        continue

    if (calcular_digito(cpf[:9], 10)) != (int(cpf[9])):
        mensagem_erro('CPF inválido! O primeiro dígito verificador está incorreto.')
        continue
    
        
    if (calcular_digito(cpf[:10], 11)) != (int(cpf[10])):
        mensagem_erro('CPF inválido! O segundo dígito verificador está incorreto.')
        continue
        
    break

print()
print('='*25)
print('O CPF informado é válido!')
print('='*25)
print()

