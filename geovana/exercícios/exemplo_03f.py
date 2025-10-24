import os 
os.system('cls')

def boleira(a):
    print("Fazendo o bolo.")
    bolo = True
    return bolo

pedido = input("Faça um bolo!")

entrega = boleira(pedido)
print("Seu bolo está pronto! {entrega}")
