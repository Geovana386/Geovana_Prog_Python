import os 
os.system('cls')

nome = input("Digite seu nome:")
idade = int(input("Digite a sua idade:"))
sexo = input("Digite o seu sexo:")

sexo2 = sexo.lower()

if(sexo2 == "f" and idade < 25):
    print(f"A aluna {nome} foi ACEITA")
else:
    print(f"A aluna {nome} foi NÃO ACEITA")   
