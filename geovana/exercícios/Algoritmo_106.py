import os 
os.system('cls')

nome = input("Digite um nome:")

primeiro_carac = nome[0]

#print(primeiro_carac)

if(primeiro_carac == "A"):
    print(nome)
else:
    print("Não começa com a letra A")


#PROFESSOR

import os 
os.system('cls')

nome = input("Digite um nome:")

if(nome[0].upper() == "A"):
    print(nome)