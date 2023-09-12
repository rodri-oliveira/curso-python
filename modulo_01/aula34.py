qtd_linhas = 10
qtd_colunas = 10

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha} x {coluna} = {linha * coluna} ')
        coluna += 1
    print('\n')
    linha += 1


print('Acabou')