

import os 
os.system('cls')

nota_01 = 7
nota_02 = 8
nota_03 = 2
nota_04 = 6

media = (nota_01+nota_02+nota_03+nota_04)/4

if(media >= 7):
    print("Aluno promovido com sucesso")
elif (media >= 5 and media < 7):
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")    

print(media)    