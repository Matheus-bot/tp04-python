print('='*40)
print('MATHEUS HENRIQUE DE CAMPOS RUMÃO ')
print('RA: 1051392421015')
print('='*40)

usuario = input('USUSARIO:')
senha = int(input('SENHA:'))

user = 'professor'
passw = 123

if (user == usuario) and (senha == passw):
    print('='*40)
    print('SEJA BEM VINDO PROFESSOR: ')
    print('='*40)
    nome = input('Qual o nome do aluno ? ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    mg = (nota1*4 + nota2*6) / 10 
    print('A situação do aluno {} foi:'.format(nome))
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
else: 
    print('Voçê não está autorizado para ver essa nota!!!')