import os 
os.system('cls')

pessoa = {
    "nome": "Ana",
    "idade": 30,
    "cidade": "São Paulo"
}


pessoa["nome"]="Paula"
print(pessoa)

pessoa.update({"estado":"SP"})
print(pessoa)

pessoa.update({"endereço":"Java Ali, 74","CEP":"0896-500"})
print(pessoa)

pessoa.pop("cidade")
print(pessoa)

pessoa.popitem()
print(pessoa)

del pessoa ["endereço"]
print(pessoa)

pessoa.clear
print(pessoa)

print(len(pessoa))
