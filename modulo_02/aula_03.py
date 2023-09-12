

def criar_saudacao(saudacao, nome):
    return f'{saudacao}, {nome}'

pessoa_1 = criar_saudacao('ola', 'Rodrigo')
pessoa_2 = criar_saudacao('ola', 'Rogerio')

print(pessoa_1,'\n' ,pessoa_2)