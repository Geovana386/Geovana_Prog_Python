import os
os.system('cls')

numero_01 = int(input("Digite um número:"))
numero_02 = int(input("Digite outro número:"))
numero_03 = int(input("Digite mais um número:"))

if(numero_01 > numero_02):
    print(f"O número {numero_01} é o maior dos três")
elif(numero_02 > numero_03):
    print(f"O número {numero_02} é o maior dos três")
else:
    print(f"O número {numero_03} é o maior dos três")        