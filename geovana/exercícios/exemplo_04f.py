import os
os.system('cls')
import math

def somar(a,b):
    total = a+b
    print(total)

def subtrair(a,b):
    total = a-b
    print(total) 

def multiplicar(a,b):
    total = a*b
    print(total)       

def dividir(a,b):
    total = a/b
    print(total)    

numero_01 = int(input("Digite um número:"))
numero_02 = int(input("Digite um número:"))

somar(numero_01,numero_02)
subtrair(numero_01,numero_02)
multiplicar(numero_01,numero_02)
dividir(numero_01,numero_02)
