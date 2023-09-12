pessoa = {
    'nome': 'Rodrigo de Oliveira',
    'sobrenome': 'Miranda',
    'idade': 23,
    'endereco': {
        'rua1': 'certo',
        'rua2': 'errado',
        'complemento': {
            'casa2': 'sem campanhia',
            'casa3': 'com campanhia',
        }
    }
}

print(pessoa['endereco']['complemento']['casa2'])

# print(pessoa.__len__())
# print(len(pessoa))
# print(pessoa.keys())
# print(list(pessoa.values()))

# for chave, valor in pessoa.items():
#     print(chave,valor)

teste1 = pessoa.get('idade', 'não tem esta chave')
print(teste1)

teste2 = pessoa.setdefault('idade', 'não tem este valor')
print(teste2)

d1 = pessoa.copy()
print(d1)

