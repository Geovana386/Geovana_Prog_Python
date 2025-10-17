import os 
os.system('cls')

nome = input("Digite um nome:")

if(nome == "José"):
   print(nome.upper())
else:
   print("Nome inválido")   


#PROFESSOR

nome = input("Digite um nome:")

if(nome.upper() in ["JOSÉ","JOSE"]):
    print(nome)
else:
   print("Não começa com José")    