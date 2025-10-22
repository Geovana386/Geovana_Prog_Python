import os 
os.system('cls')
import time

numero01 = -1
cont = 0

while(True):
    numero7 = int(input("Digite um número:"))
    if(numero7 < numero01):
        break
    else:
        cont = numero7
        print(f"Foram digitados {cont} números")


#PROFESSOR 

cont = 0

while(True):
    numero = int(input("Digite um número:"))
    if(numero < 0):
        break
    cont += 1
print(f"A quantidade de números digitados foi: {cont}")    
