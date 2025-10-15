import os
os.system('cls')

ano_nascimento = int(input("Digite seu ano de nascimento:"))
ano_atual = int(input("Digite o ano atual:"))

if(ano_atual - ano_nascimento != 0 and ano_atual-ano_nascimento <= 100):
   idade = ano_atual-ano_nascimento
   print(f"idade é: {idade}")
else: 
   print(f"Ano inválido")


