def soma(*args):
    total = 0
    for item in args:
        total += item
    return total
result = soma(1,2,3,4,5,6)

print(result)


soma2 = (1,2,3,4,5,6,7,8,9)
result2 = sum(soma2)
print(result2)