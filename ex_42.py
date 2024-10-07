print('='*40)
print('MATHEUS HENRIQUE DE CAMPOS RUMÃO ')
print('RA: 1051392421015')
print('='*40)


contador = 0
maior = 0

while contador < 5:
    nota = float(input('Digite a nota do aluno {}° aluno: ' .format(contador + 1 )))
    
    if nota > maior:
        maior = nota
    contador += 1  

print('A maior nota da turma é: ', maior)
