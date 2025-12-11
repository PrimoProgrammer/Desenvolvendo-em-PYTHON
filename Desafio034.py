salario = float(input('Qual o salário do funcionário? '))

if salario >= 1250.00:
    #novo = salario + (salario*10/100) possibilidade de fazer
    print('Para salários superior a R$1250,00, receberá 10% de aumento. '
          'De R${:.2f}, receberá R${:.2f} !'.format(salario, (salario+salario*10/100)))
if salario < 1250.00:
    # novo = salario + (salario*15/100) possibilidade de fazer
    print('Já para salário inferior a R$1250,00, receberá 15% de aumento.'
          'De R${:.2f}, receberá R${:.2f} !'.format(salario, salario+salario*15/100))