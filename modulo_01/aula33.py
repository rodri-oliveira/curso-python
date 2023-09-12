numero_tabuada = input('Digite o numero para tabuada: ')
numero_tabuada_inteiro = int(numero_tabuada)
contador_2 = 1


while contador_2 <= 10:
    print(f'{numero_tabuada} x {contador_2} = {numero_tabuada_inteiro * contador_2}')
    contador_2 += 1