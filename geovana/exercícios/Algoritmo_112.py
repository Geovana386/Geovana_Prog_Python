import os
os.system('cls')

numero_01 = int(input("Digite um número:"))
numero_02 = int(input("Digite mais um número:"))

if(numero_01 < numero_02):
    print(f"O número menor é o {numero_01}")
else:
    print(f"O número menor é o {numero_02}")    