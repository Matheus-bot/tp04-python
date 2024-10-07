print('='*40)
print('MATHEUS HENRIQUE DE CAMPOS RUMÃO ')
print('RA: 1051392421015')
print('='*40)

print('='* 30)
print('exercício 40')
print('CALCULO DE AUMENTO DE SALÁRIO:')
print('='* 30)

salario = float(input('Qual seu salário: '))

if (salario <= 1500):
    aumento = salario * (20 / 100)
    novo_salario = salario + aumento 
    print('Seu salário com 20 % de aumento agora é R${:.2f} ' .format(novo_salario))
elif (salario > 1500 ) and (salario < 2500):
    aumento = salario * (15 / 100)
    novo_salario = salario + aumento 
    print('Seu salário com o aumento de 15 % agora é R${:.2f} ' .format(novo_salario))
else:
    aumento = (5/ 100) * salario
    novo_salario = salario + aumento 
    print('Seu salário com 5 % de aumento agora é R${:.2f}' .format(novo_salario))