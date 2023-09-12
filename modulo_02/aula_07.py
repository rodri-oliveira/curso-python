# s1 = {1,2,3,4,4,4,4,4}

# s2 = set(s1)

# print(s2)

s1 = {1,2,3,4}
s2 = {2,3,5,6,}

s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2

print(s3)
print(s4) # intersecção (mostra os dados presentes nos dois sets)
print(s5) # mostra os dados que não tem no segundo set
print(s6) # retorna os dados que não estão presentes em ambos





