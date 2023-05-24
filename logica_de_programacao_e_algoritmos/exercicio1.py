estudante = 'João Gabriel Zeba de Souza'
ru = 4040238
print('Bem Vindo a Loja do', estudante)  # Identificação pessoal
valor_do_produto = float(input('Entre com o valor do produto: '))  # Recebe o valor unitário do produto
quantidade = int(input('Entre com o valor da quantidade: '))  # Conta a quantidade do produto
desconto = 0  # Percentual de desconto
if quantidade >= 1000:
    desconto = 0.15  # Há 15% de desconto
elif quantidade >= 100:
    desconto = 0.1  # Há 10% de desconto
elif quantidade >= 10:
    desconto = 0.05  # Há 5% de desconto
else:
    desconto = 0  # Não há desconto
sub_total = valor_do_produto * quantidade  # Valor sem desconto
total = sub_total - (sub_total * desconto)  # Valor com desconto
print('O valor sem desconto foi: R${:.2f}' .format(sub_total))
print('O valor com desconto foi: R${:.2f}' .format(total), '(desconto {}%)' .format(int(desconto * 100)))
