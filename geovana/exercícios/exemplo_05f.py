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
op = input("Digite a operação")
if op == "+":
   somar(numero_01,numero_02)
elif (op == "-"):
    subtrair(numero_01,numero_02)
elif (op == "*"):
    multiplicar(numero_01,numero_02)
elif (op == "/"):
    dividir(numero_01,numero_02)
else:
    print("Operação Inválida")               

