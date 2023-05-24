estudante = 'João Gabriel Zeba de Souza'
ru = 4040238
print('Bem Vindo a Companhia de Logística', estudante)  # Identificação pessoal


def dimensoes_objeto():  # Função que determina o valor cobrado pela caixa de acordo com o volume do objeto
    volume = 0  # Receberá o resultado da multiplicação dos dados (altura, comprimento e largura) inseridos pelo usuário
    while True:
        try:  # Evita o erro no caso do usuário atribuir um valor inválido a alguma variável
            altura = int(input('Digite a altura do objeto (em cm): '))
            comprimento = int(input('Digite o comprimento do objeto (em cm): '))
            largura = int(input('Digite a largura do objeto (em cm): '))
            volume = altura * comprimento * largura
        except ValueError:  # Indica como proceder caso ocorra essa exceção
            print('Você digitou alguma dimensão do objeto com valor não numérico.')  # Mensagem de erro
            print('Por favor, entre com as dimensões desejadas novamente.')
            continue  # Volta para o início do laço
        if volume > 100000:  # Verifica se o volume é maior do que o limite máximo aceito
            print('O volume do objeto é (em cm³): {}'.format(int(volume)))
            print('Não aceitamos objetos com dimensões tão grandes.')  # Mensagem de erro
            print('Por favor, entre com as dimensões desejadas novamente.')
            continue  # Volta para o início do laço
        else:
            print('O volume do objeto é (em cm³): {}' .format(int(volume)))
            break  # Encerra o loop
    if volume > 30000:  # Primeiro teste para saber qual valor cobrar pelo tamanho da caixa
        valor = 50
    elif volume > 10000:
        valor = 30
    elif volume > 1000:
        valor = 20
    else:  # Último teste
        valor = 10
    return valor  # Retorna o resultado da função


def peso_objeto():  # Função para determinar um multiplicador de acordo com o peso do objeto
    peso = 0  # Receberá o valor inserido pelo usuário
    while True:
        try:  # Evita o erro no caso do usuário atribuir um valor inválido à variável
            peso = float(input('Digite o peso do objeto (em Kg): '))
        except ValueError:  # Indica como proceder caso ocorra essa exceção
            print('Você digitou um valor não numérico.')  # Mensagem de erro
            print('Por favor, entre com o peso desejado novamente.')
            continue  # Volta para o início do laço
        if peso > 30:  # Verifica se o peso é maior do que o limite máximo aceito
            print('Não aceitamos objetos tão pesados.')  # Mensagem de erro
            print('Por favor, entre com o peso desejado novamente.')
            continue  # Volta para o início do laço
        else:
            break  # Encerra o loop
    if peso > 10:  # Primeiro teste para saber qual valor atribuir ao multiplicador
        mult_p = 3
    elif peso > 1:
        mult_p = 2
    elif peso > 0.1:
        mult_p = 1.5
    else:  # Último teste
        mult_p = 1
    return mult_p  # Retorna o resultado da função


def rota_objeto():  # Função para determinar um multiplicador de acordo com a rota desejada
    while True:
        print('Selecione a rota:')
        print('BR - De Brasília para Rio de Janeiro')
        print('BS - De Brasília para São Paulo')
        print('RB - De Rio de Janeiro para Brasília')
        print('RS - De Rio de Janeiro para São Paulo')
        print('SB - De São Paulo para Brasília')
        print('SR - De São Paulo para Rio de Janeiro')
        rota = input().upper()  # Entra a rota desejada pelo usuário
        mult_r = 0  # Multiplicador com base na rota
        if rota == 'RS' or rota == 'SR':  # Primeira verificação para saber qual valor atribuir ao multiplicador
            mult_r = 1
        elif rota == 'BS' or rota == 'SB':
            mult_r = 1.2
        elif rota == 'BR' or rota == 'RB':  # Última verificação
            mult_r = 1.5
        else:  # Indica que a rota inserida pelo usuário não é válida
            print('Você digitou uma rota que não existe.')  # Mensagem de erro
            print('Por favor, entre com a rota desejada novamente.')
            continue  # Volta para o início do laço
        break  # Encerra o loop
    return mult_r  # Retorna o resultado da função


vlrVolume = dimensoes_objeto()  # Valor da caixa
multPeso = peso_objeto()  # Multiplicador peso
multRota = rota_objeto()  # Multiplicador rota
total = vlrVolume * multPeso * multRota  # Valor total a ser pago
print('Total a pagar: R${:.2f} (dimensões: {} * peso: {} * rota: {})' .format(total, vlrVolume, multPeso, multRota))
