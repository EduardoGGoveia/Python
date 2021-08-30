# Exemplos aula 7
var = 5 + 2 * 3
print(var)
var = 3 * 5 + 4 ** 2
print(var)
var = 3 * (5 + 4) ** 2
print(var)
print('=' * 75)

r = 'Eduardo'
print('Prazer em te conhecer {:=^20}!'.format(r), end=' ')
r = 'Beatriz'
print('Prazer em te conhecer {:->20}!'.format(r))
r = 'Viviane'
print('Prazer em te conhecer {:´<20}'.format(r))
print('-' * 75)

# n1 = int(input('Um valor: '))
# n2 = int(input('Outro valor: '))
n1 = 5
n2 = 10
print('A soma é: {}'.format(n1 + n2))
print('/' * 75)

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
exp = n1 ** n2
print('A soma entre {} e {} \né igual a {}'.format(n1, n2, s), end=' ')
print('-' * 1)
print('=' * 20)
print('A multiplicação entre {} e {} \né igual a {}'.format(n1, n2, m))
print('=' * 20)
print('A divisão entre {} e {} \né igual a {:.2f}'.format(n1, n2, d))
print('=' * 20)
print('A divisão inteira entre {} e {} \né igual a {}'.format(n1, n2, di))
print('=' * 20)
print('A potenciação de base {} e expoente  {} \né igual a {}'.format(n1, n2, exp))
print('=' * 20)
