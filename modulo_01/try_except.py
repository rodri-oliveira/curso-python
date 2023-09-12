# introdução ao try / except

numero = input('Vou dobrar seu numero')

try:
    print('STR:', numero)
    numero_float = float(numero)
    print('numero float:', numero_float)
    print(f'o dobro do numero {numero_float} é {numero_float * 2}')
except:
    print('Não é um numero: ')


