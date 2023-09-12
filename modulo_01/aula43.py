salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luis', 'João', 'Eduardo', (0,1,2,3)],
]

# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][0])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)