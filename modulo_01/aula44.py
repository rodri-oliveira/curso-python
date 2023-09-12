string = 'ABSD'
lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']
tupla = 'python', 'é', 'legal'

p, b, *resto, u = lista

# print(p, *resto)

# for item in lista:
#     # print(item, end=' ')

# print(*lista)

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luis', 'João', 'Eduardo', (0,1,2,3)],
]

# print(*salas, end='\n')
# print(*salas, sep='\n')
print(*salas[0], sep='\n')