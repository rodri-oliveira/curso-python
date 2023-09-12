valor = [1,2,3,4,5,6]
acc = 0

for item in valor:
    print(item)
    acc += item
    
print(acc)

# def soma (a, b):
#     return a + b


from functools import reduce
result = reduce((lambda i, j:  (i * j)) , valor)
print(result)

