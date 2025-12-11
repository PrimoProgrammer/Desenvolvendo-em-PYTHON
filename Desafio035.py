print('Desafio 035 - analisador de triângulo')

#regra para ter todos lados que seja possível formar um triângulo
#cada lado tem que ser menor que a soma dos outros dois
from time import sleep

c1 = float(input('Digite o primeiro comprimento: '))
c2 = float(input('Digite o segundo comprimento: '))
c3 = float(input('Digite o terceiro comprimento: '))
print('-=-'*20)
print('Analisando...')
print('-=-'*20)
sleep(3)

if c1 < c2+c3 and c2 < c1+c3 and c3 < c1 + c2:
    print('Os segmentos acima PODEM FORMAR Triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR Triângulo')

