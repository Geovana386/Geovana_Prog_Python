import os 
os.system('cls')

numero = int(input("Digite um número:"))

if(numero >= 20 and numero <= 90):
    print(f"O número {numero} está entre 20 e 90.")
else:
    print(f"O número {numero} não está entre 20 e 90.")
