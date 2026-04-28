'''
LISTA
Caracteristicas
poderosa, flexivel, performatica, conjunto de comandos para manipulação completos
MUTAVEL: depois de criada, a lista permite acrescentar, retirar, modificar elementos
EXPANSIVEL: pode aumentar seu conjunto de dados a partir de outra lista
ACEITA TIPOS DIFERENTES DE DADOS
INDEXADA: cada elemento tem uma POSIÇÃO dentro da LISTA
PERMITE DUPLICADOS
ORDENAVEIS --> a ordenação natural só acontece se todos elementos forem do mesmo tipo
SIMBOLO: []
'''

titulo = 'Listas'
print(f'{titulo:^30}')
minhaLista = ['café', 'água', 'açucar']
print(minhaLista)

#E se eu quisesse imprimir somente o café?
#Entender como acessar cada elemento pelo índice
#Toda coleção indexada começa no zero
minhaLista = ['café', 'água', 'açucar', 'canela']
print(minhaLista)
#  0        1       2         3
# -4       -3      -2        -1
#'café', 'água', 'açucar', 'canela'
print(f'primeiro elemento: {minhaLista[0]}')
print(f'segundo elemento: {minhaLista[1]}')
print(f'Tamanho da lista: {len(minhaLista)}')
print(f'Ultimo elemento: {minhaLista[3]}')
print(f'Ultimo elemento: {minhaLista[len(minhaLista)-1]}')

#Tentando acessar um indice que não existe
#print(f'Ultimo elemento: {minhaLista[5]}')

#Como acrescentar itens numa lista?
#O metodo append faz isso
print('\n')
print(minhaLista)
minhaLista.append('chantilly')
minhaLista.append('especiarias')
print(minhaLista)

#E para remover itens da lista
#Usamos o metodo pop
#Ele sem parametro remove DO FIM DA LISTA
minhaLista.pop()
print(minhaLista)
minhaLista.pop()
print(minhaLista)
#MAS EU POSSO REMOVER UM ITEM ESPECIFICO COM O POP
#BASTA PASSAR O INDICE
#Removendo o açucar
minhaLista.pop(2)
print(minhaLista)

#TOD O ELEMENTO INTERAVEL podemos percorrer através do FOR
print('Elementos um a um')
for item in minhaLista:
    print(item)
print('\n')

#Percorrendo a lista pelos INDICES da lista
for i in range(len(minhaLista)):
    print(minhaLista[i])