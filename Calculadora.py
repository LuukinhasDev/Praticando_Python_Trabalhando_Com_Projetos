def ler_numero(pergunta):
    while True:
        texto = input(pergunta).replace(",", ".")
        
        try:
            return float(texto)
        except ValueError:
            print('ERRO! Entrada inválida. Digite apenas números válidos')

def ler_operador():
    operadores = ['+', '-', '*', '**', '/', '%']
    while True:
        operacao = input('\nEscolha uma operação (+, -, *, **, /, %): ').strip()

        if operacao not in operadores:
            print('Operação Inválida')
            continue

        return operacao

def calcular(n1, operacao, n2):
    match operacao:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "**":
            return n1 ** n2
        case "/":
            return n1 / n2
        case "%":
            return n1 % n2
        

def calculadora():
    primeiro = ler_numero('\nDigite o primeiro número: ')
    operacao = ler_operador()
    
    while True:
        
        segundo = ler_numero('\nDigite o segundo número: ')
        try:
            return f'\nResultado: {calcular(primeiro, operacao, segundo):.2f}'
        
        except ZeroDivisionError:
            print('ERRO: Não é possível dividir por zero.')

        except OverflowError:
            print('ERRO: o resultado é grande demais para ser calculado.')
            

print(calculadora())