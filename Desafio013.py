print('==== Salário novo do funcionário com aumento este ano! ====')

salario = float(input('Digite o salário do funcionário: '))
aumento = float(15/100)
salarioatual = (salario * aumento + salario)

print('O novo salário do funcionário será de R$ {:.2f} reais!'.format(salarioatual))

