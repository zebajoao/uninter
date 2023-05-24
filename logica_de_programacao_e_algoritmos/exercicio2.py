estudante = 'João Gabriel Zeba de Souza'
ru = 4040238
print('Bem Vindo a Lanchonete do', estudante)  # Identificação pessoal
print('********************Cardápio*********************')
print('|  Código  |       Descrição       | Valor (R$) |')
print('|    100   |    Cachorro Quente    |     9.00   |')
print('|    101   | Cachorro Quente Duplo |    11.00   |')
print('|    102   |        X-Egg          |    12.00   |')
print('|    103   |        X-Salada       |    12.00   |')
print('|    104   |        X-Bacon        |    14.00   |')
print('|    105   |        X-Tudo         |    17.00   |')
print('|    200   |   Refrigerante Lata   |     5.00   |')
print('|    201   |       Chá Gelado      |     4.00   |')
sub_total = 0  # Acumula os valores dos lanches
while True:
    pedido = input('Entre com o código do produto desejado: ')  # Usuário entra com o código de um produto
    if pedido == '100':  # Primeira verificação de validade do código inserido pelo usuário
        sub_total += 9
        print('Você pediu um Cachorro Quente no valor de R$9.00')
    elif pedido == '101':
        sub_total += 11
        print('Você pediu um Cachorro Quente Duplo no valor de R$11.00')
    elif pedido == '102':
        sub_total += 12
        print('Você pediu um X-Egg no valor de R$12.00')
    elif pedido == '103':
        sub_total += 12
        print('Você pediu um X-Salada no valor de R$12.00')
    elif pedido == '104':
        sub_total += 14
        print('Você pediu um X-Bacon no valor de R$14.00')
    elif pedido == '105':
        sub_total += 17
        print('Você pediu um X-Tudo no valor de R$17.00')
    elif pedido == '200':
        sub_total += 5
        print('Você pediu um Refrigerante Lata no valor de R$5.00')
    elif pedido == '201':  # Última verificação
        sub_total += 4
        print('Você pediu um Chá Gelado no valor de R$4.00')
    else:  # Entrada de código inválida
        print('Opção Inválida')  # Mensagem de erro
        continue  # Retorna ao início do laço
    print('Deseja pedir mais alguma coisa?')
    print('1 - Sim')
    print('0 - Não')
    novo_pedido = int(input())
    if novo_pedido == 1:  # Identifica se o usuário quer fazer mais algum pedido
        continue  # Retorna ao início do laço
    else:
        break  # Encerra o loop
print('O total a ser pago é: R${:.2f}' .format(float(sub_total)))
