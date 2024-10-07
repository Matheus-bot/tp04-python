print('='*40)
print('MATHEUS HENRIQUE DE CAMPOS RUMÃO ')
print('RA: 1051392421015')
print('='*40)

sexo = input('Digite seu sexo [M|F]')

if (sexo == 'M') or (sexo == 'm'):
    altura = float(input('Qual sua altura? '))
    peso = float(input('Qual seu peso? '))
    imc = peso /(altura * altura)
    if imc < 20:
        print('Você esta abaixo do peso!!!')
    elif (imc >= 20) and (imc < 25):
        print('Você esta no peso ideal')
    elif (imc >= 25): 
        print('Você esta acima do peso!!!')
elif (sexo == 'F') or (sexo == 'f'):
    altura = float(input('Qual sua altura? '))
    peso = float(input('Qual seu peso? '))
    imc = peso / (altura * altura)
    if imc < 19:
        print('Você esta abaixo do peso!!!')
    elif (imc >= 19) and (imc < 24):
        print('Você esta no peso ideal')
    elif (imc >= 24): 
        print('Você esta acima do peso!!!')
else:
    print('Você deve digitar apenas M ou F ')