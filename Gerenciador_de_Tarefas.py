import os

lista_de_tarefas = []

def exibe_nome_do_programa():
    print(''' 
█████▀██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▀█▄─▄█─▄▄▄─█▄─▄██▀▄─██▄─▄▄▀█─▄▄─█▄─▄▄▀███▄─▄▄▀█▄─▄▄─█
█─██▄─██─▄█▀██─▄─▄██─▄█▀██─█▄▀─██─███▀██─███─▀─███─██─█─██─██─▄─▄████─██─██─▄█▀█
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀
███████████████████████████████████████████
█─▄─▄─██▀▄─██▄─▄▄▀█▄─▄▄─█▄─▄▄─██▀▄─██─▄▄▄▄█
███─████─▀─███─▄─▄██─▄█▀██─▄████─▀─██▄▄▄▄─█
▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀ \n''')

def exibir_subtitulos(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def sair():
    exibir_subtitulos('Finalizando Gerenciador de Tarefas. Até a próxima!')

def opcao_invalida(texto):
    print(texto)
    voltar_ao_menu()

def voltar_ao_menu():
    input('Pressione ENTER para voltar ao menu principal.')

def exibir_opcoes():
    print()
    print('1. Adicionar tarefa')
    print('2. Visualizar tarefas')
    print('3. Remover tarefa')
    print('4. Sair\n')


def adiciona_tarefa():

    exibir_subtitulos('ADICIONAR TAREFA')

    while True:
        tarefa = str(input('Digite o nome da tarefa que você deseja adicionar: ')).upper().strip()

        if tarefa == '':
            print('\nERRO! Entrada Vazia. digite uma tarefa para ser adicionada na lista.\n')
            continue

        descricao_tarefa = str(input('Descreva brevemente essa tarefa se desejar: ')).lower()
        dados_tarefa = {'nome': tarefa, 'descrição': descricao_tarefa}
        lista_de_tarefas.append(dados_tarefa)
        print(f"\nA tarefa |{dados_tarefa['nome']}| foi adicionada com sucesso!\n")
        
        break
    voltar_ao_menu()

def visualizar_tarefas():

    exibir_subtitulos('MINHAS TAREFAS')
    if not lista_de_tarefas:
        print('\nNão existe nenhuma tarefa na lista neste momento.\n')
        voltar_ao_menu()
        return

    mostrar_tarefas_numeradas()    
    voltar_ao_menu()
    

def mostrar_tarefas_numeradas():
    for numero, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f"{numero}. {tarefa['nome']} | {tarefa['descrição']}")
        print()

def remover_tarefa():
    exibir_subtitulos('REMOVER TAREFAS')

    if not lista_de_tarefas:
        print('\nNão há tarefas na lista para remover.\n')
        voltar_ao_menu()
        return
    mostrar_tarefas_numeradas()

    while True:
        try:
            numero = int(input('Digite o número da tarefa que deve ser removida: '))
        except ValueError:
            print('\nERRO: Digite apenas o número da tarefa.\n')
            continue

        if numero < 1 or numero > len(lista_de_tarefas):
            print(f'\nERRO: escolha um número entre um e {len(lista_de_tarefas)}.\n')
            continue

        break
        
    removida = lista_de_tarefas.pop(numero - 1) 
    print(f"\nA tarefa |{removida['nome']}| foi removida da lista de tarefas com sucesso\n")     
    voltar_ao_menu()

def ler_opcao():
    try:
        return int(input('Escolha uma opção (1-4): '))
    except ValueError:
        return None
    
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibe_nome_do_programa()
        exibir_opcoes()
        opcao = ler_opcao()

        match opcao:
            case 1:
                adiciona_tarefa()
            case 2:
                visualizar_tarefas()
            case 3:
                remover_tarefa()
            case 4:
                sair()
                break
            case _:
                opcao_invalida('\nOPÇÃO INVÁLIDA. Escolha uma das opções de 1 a 4!\n')

if __name__ == '__main__':
    main()