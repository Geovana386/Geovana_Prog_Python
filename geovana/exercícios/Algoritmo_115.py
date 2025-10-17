import math
import os
os.system('cls')

numero_01 = int(input("Digite um número:"))
numero_02 = int(input("Digite mais um número:"))

if(numero_01 < numero_02):
    print(f"O quadrado do menor número é {numero_01*numero_01} e a raiz quadrada do maior é {math.sqrt(numero_02)}")
else:
    print(f"O quadrado do menor número é {numero_02*numero_02} e a raiz quadrada do maior é {math.sqrt(numero_01)}")


#elif(numero_01 > numero_02):
    #print(f"A raiz quadrada do maior número é {math.sqrt(numero_01)}")


