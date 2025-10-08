

import os
os.system('cls')

# função len () ela conta o tamnaho da minha string
texto = "Olá Mundo!"
tamanho = len(texto)
print(f"O tamanho da string é {tamanho}")

# texto todo em letra maiúscula
texto_maiusculo = texto.upper()
print(f"O texto em letra maiuscula {texto_maiusculo}")

# texto todo em letra minuscula
texto_minusculo = texto.lower()
print(f"O texto em letra minuscula {texto_minusculo}")

# invertendo a posicao da string 
texto_invertido = texto[::-1]
print(f"string invertida é {texto_invertido}")
