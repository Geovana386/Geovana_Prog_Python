import os
os.system('cls')

frutas = ["maça", "banana", "laranja" , "uva"]
numeros = [1,2,3,4,5,6]
mista = [1,"texto", 3.14, True]

print(frutas[0])
print(frutas[-1])
print(frutas[1:3])

frutas.append("abacaxi")
print(frutas)
print(frutas[-1])

frutas.insert(2,"kiwi")
print(frutas)

numeros.append(7)
print(numeros)

numeros.insert(0,0)
print(numeros)

frutas.remove("maça")
print(frutas)
