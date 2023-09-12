letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())
    
    
    if 'n' in letras:
        print('Voce encontrou: ')
        break
    
    print(letras)
    