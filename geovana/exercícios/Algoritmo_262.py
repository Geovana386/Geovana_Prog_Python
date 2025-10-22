import os
os.system('cls')
import time

while(True):
    numero = int(input("Digite um número:"))
    if(numero == -999):
        break
    else:
        numero = numero*3
        print(f"Triplo: {numero}")
