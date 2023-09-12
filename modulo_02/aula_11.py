produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 24},
    {'nome': 'p3', 'preco': 66},
    {'nome': 'p4', 'preco': 78},
]

# novos_produtos = [produto['preco'] * 2 for produto in produtos]
# print(*novos_produtos, sep='\n')

# novos_produtos_2 = [
#     {'nome': produto['nome'], 'preco': produto['preco'] }
#     for produto in produtos
# ]
# print(*novos_produtos_2, sep='\n')

novos_produtos_3 = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 30 else {**produto}
    for produto in produtos
]
print(*novos_produtos_3, sep='\n')