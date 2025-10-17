import os
os.system('cls')

nome_01 = input("Digite um nome:")
nome_02 = input("Digite mais um nome:")

primeiro_carac_nome_01 = nome_01[0]
primeiro_carac_nome_02 = nome_02[0]

#print(primeiro_carac_nome_01)
#print(primeiro_carac_nome_02)
#nomes = [nome_01,nome_02]

if(primeiro_carac_nome_01 > primeiro_carac_nome_02):
    print(nome_01,nome_02)
else:
    print(nome_02,nome_01)    

#PROFESSOR

nome_01 = input("Digite um nome:")
nome_02 = input("Digite mais um nome:")

if(nome_01 < nome_02):
    print(nome_01)
    print(nome_02)
else:
    print(nome_02)
    print(nome_01)
