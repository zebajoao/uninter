estudante = 'João Gabriel Zeba de Souza'
ru = 4040238
lista_pecas = []  # Lista de peças cadastradas
contador = 0  # Variável contadora, registra a quantidade de cadastros feitos


def cadastrar_pecas(codigo):  # Função que realiza o cadastro das peças, o parâmetro varia conforme o "contador"
    print('Você selecionou a opção de cadastramento de peças.\n'
          'Código da Peça: {}'.format(str(codigo).rjust(3, '0')))
    nome = input('Por favor, insira o NOME da peça: ')  # Usuário entra com as informações
    fabricante = input('Por favor, insira o FABRICANTE da peça: ')
    while True:
        try:  # Verifica a entrada de caracteres não numéricos
            valor = float(input('Por favor, insira o VALOR (R$) da peça: '))
        except ValueError:
            print('Você inseriu um valor não numérico.\nPor favor, tente novamente.')  # Mensagem de erro
            continue  # Retorna ao início do laço
        break  # Encerra o loop
    dicionario_pecas = {'Código': str(codigo).rjust(3, '0'),  # Armazena os dados das peças cadastradas
                        'Nome': nome,
                        'Fabricante': fabricante,
                        'Valor': 'R${:.2f}' .format(valor)}
    lista_pecas.append(dicionario_pecas.copy())  # Atualiza a lista de peças cadastradas
    print('Cadastro concluído.')


def consultar_pecas():  # Função que busca e imprime na tela dados armazenados na lista
    print('Você selecionou a opção de consulta de peças.')
    while True:
        try:  # Verifica a entrada de caracteres não numéricos
            sub_menu = int(input('Escolha a opção desejada:\n'
                                 '1 - Consultar todas as peças\n'
                                 '2 - Consultar peças por código\n'
                                 '3 - Consultar peças por fabricante\n'
                                 '4 - Retornar\n'
                                 '>> '))
        except ValueError:
            print('Opção inválida.\nPor favor, tente novamente.')
            continue
        if sub_menu == 1:  # Primeira verificação de opção selecionada pelo usuário
            for peca in lista_pecas:
                print('-' * 20)
                for key, value in peca.items():
                    print('{}: {}'.format(key, value))  # Imprime na tela toda a lista de peças cadastradas
                print('-' * 20)
            continue
        elif sub_menu == 2:
            consulta_codigo = str(input('Digite o código da peça: ')).rjust(3, '0')  # Solicita o código do produto
            for peca in lista_pecas:  # Verifica todos os dicionários da lista
                if peca['Código'] == consulta_codigo:  # Verificação de igualdade entre o dado inserido e o da chave
                    print('-' * 20)
                    for key, value in peca.items():
                        print('{}: {}'.format(key, value))  # Imprime o dicionário que satisfaz à condição
                    print('-' * 20)
            continue
        elif sub_menu == 3:
            consulta_fabricante = input('Digite o fabricante da peça: ')  # Solicita o fabricante do produto
            for peca in lista_pecas:
                if peca['Fabricante'] == consulta_fabricante:  #
                    print('-' * 20)
                    for key, value in peca.items():
                        print('{}: {}'.format(key, value))
                    print('-' * 20)
            continue
        elif sub_menu == 4:  # Última verificação
            break  # Encerra o loop
        else:
            print('Opção inválida.\nPor favor, tente novamente.')
            continue


def remover_pecas():  # Função que remove um dicionário da lista
    print('Você selecionou a opção de remoção de peças.')
    for peca in lista_pecas:
        print('-' * 20)
        for key, value in peca.items():
            print('{}: {}'.format(key, value))  # Imprime na tela todos os produtos e informações cadastrados
        print('-' * 20)
    remocao_codigo = str(input('Digite o código da peça a ser removida: ')).rjust(3, '0')
    for peca in lista_pecas:
        if peca['Código'] == remocao_codigo:  # Define qual dicionário possui o dado da chave "código" igual ao inserido
            lista_pecas.remove(peca)  # Remove o dicionário da lista
            break


print('Bem Vindo ao Controle de Estoque da Bicicletaria do', estudante[0:4], estudante[21:26])  # Identificação pessoal
while True:
    try:  # Verifica a entrada de caracteres não numéricos
        menu_principal = int(input('Escolha a opção desejada:\n'
                                   '1 - Cadastrar Peças\n'
                                   '2 - Consultar Peças\n'
                                   '3 - Remover Peças\n'
                                   '4 - Sair\n'
                                   '>> '))
    except ValueError:
        print('Opção inválida.\nPor favor, tente novamente.')
        continue
    if menu_principal == 1:  # Primeira verificação de opção selecionada
        contador += 1  # Adiciona 1 ao valor atribuído a essa variável
        cadastrar_pecas(contador)  # Invoca a função cadastrar_pecas()
        continue
    elif menu_principal == 2:
        consultar_pecas()  # Invoca a função consultar_pecas()
        continue
    elif menu_principal == 3:
        remover_pecas()  # Invoca a função remover_pecas()
        continue
    elif menu_principal == 4:
        print('Programa encerrado.')
        break  # Encerra o programa
    else:
        print('Opção inválida.\nPor favor, tente novamente.')  # Mensagem de erro
        continue
