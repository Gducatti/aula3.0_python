import random
titulo = '20 numeros aleatorios'
print(f'{titulo:^30}')
for i in range(20):
    print(random.randint(a=1, b=50), end = ' ')