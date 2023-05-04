texto = "Não é a linguagem de programação que define o programador, mas sim sua lógica."
print(texto)
print("O texto possui", len(texto), "letras.")
from collections import Counter
texto = "Não é a linguagem de programação que define o programador, mas sim sua lógica."
counter = Counter(texto)
print("-------------------------------------------------------------------------------------------")
print(counter)