import os 
os.system('cls')

lista = []

"""for i in range(50):
    lista.append(i*2)

print(f"Exemplo lista 01 {lista}")"""    


for i in range(50):
    if(i%2!=0):
        lista.append(i)

print(f"Exemplo lista 02 {lista}") 
