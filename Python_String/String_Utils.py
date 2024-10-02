nome = "LuAn"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = " falaaa Galera "

print(texto + ".")
print(texto.strip()+ ".")
print(texto.lstrip()+ ".")
print(texto.rstrip()+ ".")

menu = "Python"

print("####" + menu + "###")
print(menu.center(14))
print(menu.center(14, "$"))

print("P-Y-T-h-o-n")

for letra in menu:
    print(letra, end="-")
print()

print("-".join(menu)) # Mesma coisa do de cima porém obviamente pior, pois ja temos a função pronta aqui