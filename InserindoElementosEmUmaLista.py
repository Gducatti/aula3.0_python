titulo = 'Cadastro de uma lista'
print(f'{titulo:^30}')

#Lista vazia
numeros = []
#Cadastro com while True / break
while True:
    n = int(input('Insira um número ou digite zero para sair: '))
    if n == 0:
        break
    numeros.append(n)
print(numeros)
#Imprimir a coleção com os elementos lado a lado
#ex: 8, 4, 6, 7
for item in numeros:
    print(item, end=', ')