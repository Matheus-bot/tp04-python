print('='*40)
print('MATHEUS HENRIQUE DE CAMPOS RUMÃO ')
print('RA: 1051392421015')
print('='*40)

num = int(input('Digite um número para calcular seu fatorial: '))

fatorial = 1 

for x in range(1, num+1):
    fatorial *= x

print('O fatorial de {} é {}' .format(num, fatorial))