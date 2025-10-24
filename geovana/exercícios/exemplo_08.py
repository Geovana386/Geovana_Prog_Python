import os
os.system('cls')

escola = {
    "Aluno_001":{
     "Nome" : "Ana Silva",
     "Idade" : 15 ,
     "Notas":{
        "Matemática" : 8.5,
        "Português" : 9.0,
        "História" : 2.0},
      
    },"Contato":{
        "email":"ana@gmail.com",
        "telefone":"1194854752"

    },
"Aluno_002":{
     "Nome" : "Vitoria Silva",
     "Idade" : 16 ,
     "Notas":{
        "Matemática" : 7.5,
        "Português" : 5.0,
        "História" : 10.0},
      
    },"Contato":{
        "email":"vic@gmail.com",
        "telefone":"11947500295"

    },

}

print(escola["Aluno_001"],["Notas"],["Matametica"])
print(escola["Aluno_002"],["Nota"],["Matematica"])

