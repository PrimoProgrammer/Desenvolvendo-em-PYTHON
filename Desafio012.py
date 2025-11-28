print('==== Desafio 12 - desconto em produto')

produto = float(input("Digite o valor do produto: "))
desconto = float (5 / 100) #5% de desconto
valortotal = float(produto - produto * desconto)

print('O novo valor do produto com desconto será de R${} reais.'.format(valortotal))





