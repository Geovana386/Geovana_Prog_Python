import os
os.system('cls')

sigla = input("Digite a sigla do seu estado:")
UF = sigla.upper

if(UF == "SP"):
    print(f"Paulista")
elif(UF == "MG"):
    print(f"Mineira")
elif(UF == "RJ"):
    print(f"Carioca")
else:
    print(f"Pertence a outros estados")      
