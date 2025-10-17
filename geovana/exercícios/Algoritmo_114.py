import os
os.system('cls')

numero_01 = int(input("Digite um número:"))
numero_02 = int(input("Digite mais um número:"))

if(numero_01 > numero_02):
    print(f"Ordem decrescente: {numero_01},{numero_02}")
else:
    print(f"Ordem decrescente: {numero_02},{numero_01}")