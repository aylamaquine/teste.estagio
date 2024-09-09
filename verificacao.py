print('-' * 30)
print('Verificação de Fibonacci')
print('-' * 30)

numero_verificar = int(input('Digite um número para verificar se pertence à sequência de Fibonacci: '))

t1 = 0
t2 = 1
encontrado = False

if numero_verificar == 0 or numero_verificar == 1:
    encontrado = True
else:
    while t2 <= numero_verificar:
        t3 = t1 + t2
        if t3 == numero_verificar:
            encontrado = True
            break
        t1 = t2
        t2 = t3

if encontrado:
    print(f'O número {numero_verificar} pertence à sequência de Fibonacci.')
else:
    print(f'O número {numero_verificar} NÃO pertence à sequência de Fibonacci.')