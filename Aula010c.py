n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {}'.format(m))
if m >= 6:
    print('Parabéns, você atingiu a média e foi aprovado!')
else:
    print('Você não atingiu a média para passar na disciplina!')

'''print('Parabéns você foi Aprovado(a)!' if m >= 6 else 'Você não passou, Estude mais!')''' #Condição simplificada