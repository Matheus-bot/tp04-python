print('='*40)
print('MATHEUS HENRIQUE DE CAMPOS RUMÃO ')
print('RA: 1051392421015')
print('='*40)

nome = input('Qual seu nome ? ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

mg = (nota1*4 + nota2*6) / 10 

if 10 > mg >= 9:
    print('CONCEITO A = APROVADO')
elif 9 > mg >= 7:
    print('CONCEITO B = APROVADO')
elif 7 > mg >= 3:
    print('CONCEITO C = EXAME')
elif 3 > mg >= 0:
    print('CONCEITO D =  DP')
else:
    print('Sua nota não se encaixa em nenhum dos conceitos ')