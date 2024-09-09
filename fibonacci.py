print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

n = int(input('Quantos termos você quer mostrar? '))
numero_verificar = int(input('Digite um número para verificar se pertence à sequência de Fibonacci: '))
t1 = 0
t2 = 1
encontrado = False
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:    
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    
    if t3 == numero_verificar:
        encontrado = True

    t1 = t2
    t2 = t3
    cont += 1

print(' -> FIM')

if encontrado or numero_verificar in (0, 1):  
    print(f'\nO número {numero_verificar} pertence à sequência de Fibonacci.')
else:
    print(f'\nO número {numero_verificar} NÃO pertence à sequência de Fibonacci.')

