# # Desenvolva um código que utilize as seguintes características de um veículo: 

# # - Quantidade de rodas; 

# # - Peso bruto em quilogramas; 

# # - Quantidade de pessoas no veículo. 

 
 

# # Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo
# # informado a partir das condições: 

# # A: Veículos com duas ou três rodas; 

# # B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg; 

# # C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg; 

# # D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; 
# # E: Veículos com quatro rodas ou mais e com mais de 6000 kg. 

# qtd_rodas = 0
# peso_bruto = 0
# qtd_pessoas_no_veiculo = 0

# while True:
#     qtd_rodas = input("Qual a quantidade de rodas em seu veiculo ? ")
#     peso_bruto = input("Qual o peso do veiculo ? ")
#     qtd_pessoas_no_veiculo = input("Qual a quantidade de pessoas que o veiculo comporta ? ")
#     if(qtd_rodas.isnumeric() == False or qtd_rodas == '') or (peso_bruto.isnumeric() == False or peso_bruto == '') or (qtd_pessoas_no_veiculo.isnumeric == False or qtd_pessoas_no_veiculo == '' ):
#         print("Dados invalidos, apenas numeros: ")
#         continue 
#     if(int(qtd_rodas) <= 3):
#         print("Sua categoria é A")
#         break
#     elif(int(qtd_rodas) == 4) and (int(qtd_pessoas_no_veiculo) <= 8) and (int(peso_bruto) <= 3500):
#         print("Sua categoria é B")
#         break
#     elif(int(qtd_rodas) >= 4) and (int(peso_bruto) >= 3500 and int(peso_bruto) <= 6000):
#         print("Sua categoria é C")
#         break
#     elif(int(qtd_rodas) >= 4) and (int(qtd_pessoas_no_veiculo) > 8):
#         print("Sua categoria é D")
#         break
#     elif(int(qtd_rodas) >= 4) and (int(peso_bruto) > 6000):
#         print("Sua categoria é E")
#         break
#     else:
#         print("Dados incorretos, tente novamente : ")
#         continue

def num_divisivel(num):
  if(num % 2 == 0):
    print(f'o {num} é divisivel por 2')
  elif (num % 3 == 0):
    print(f'o {num} é divisilvel por 3')
  else:
    print('Não é divisivel por 2 ou por 3 : ')

while True:
  try:
    num = input('Digite um numero: ')
    num_int = int(num)
    num_divisivel(num)
  except:
    print('Dados incorretos: ')



        