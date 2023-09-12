# iterando com in

nome = input('Digite seu nome: ')
encontrar = input('O que deseja encontrar no nome: ')

if encontrar in nome:
    print(f'{encontrar} esta em nome.')
else:
    print(f'{encontrar} não esta em nome. ')