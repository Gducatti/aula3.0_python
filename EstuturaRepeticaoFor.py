'''
Há uma outra estrutura de repetição que serve para quando
sabemos de antemão quantas repetições vamos ter
FOR
--> percorre ELEMENTOS ITERAVEIS
'''
titulo = 'Estutura Repetição FOR'
print(f'{titulo:^30}')
titulo = 'TABUADA'
print(f'{titulo:^30}')
#Enquanto o while nós temos que controlar o contador
#O for faz isso de maneira automatica
n = int(input('Entre com um número inteiro para a tabuada: '))
for numero in (1,2,3,4,5,6,7,8,9,10):
    tabuada = n * numero
    print(f'{n} X {numero} = {tabuada}')

#Existe uma maneira de abreviar essa lista de números
#É o comando RANGE
#Range nada mais é que um gerador de números de um intervalo
#1a maneira de uso é passar a quantidade de números necessários
print('Gerando 5 números')
for i in range(5):
    print(i)

#Será que o range pode gerar os números a partir de um número escolhido?
#Por exemplo a partir do 1
#2a maneira - passando o inicio e o final
print('Gerando 5 números')
#Desse jeito ele comeu o ultimo numero
for i in range(1,5):
    print(i)
#Corrigindo
print('\n')
for i in range(1,6):
    print(i)
print('\n')
for i in range(1,5+1):
    print(i)

#Existe mais um parametro no range
#o ultimo parametro chamamos de incremento ou pulo
print('Gerando 5 numeros a partir de um inicio e com pulo de 2 (até o número 5')
#Desse jeito ele comeu o ultimo número
for i in range(1,5+1,2):
    print(i)

#Tabuada usando o comando range
n = int(input('Entre com um número inteiro para a tabuada: '))
for numero in range(1,10+1):
    tabuada = n * numero
    print(f'{n} X {numero} = {tabuada}')