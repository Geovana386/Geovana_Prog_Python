import os 
os.system('cls')
import time

cont = 0
acm = 0

while(True):
    numero = int(input("Digite um número:"))
    if(numero == 0):
        break
    acm = acm+numero
    cont = cont +1

média = acm/cont
print(f"Tptal: {acm}, média: {média}")    
