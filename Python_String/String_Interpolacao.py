nome = "Luan"
idade = 23
profissao = "procurando..."
linguagem = "Python"
saldo = 1.029

dados = {"nome": "Luan", "idade": 23}

print("Nome: %s \nIdade: %d" % (nome, idade))
print("Nome: {} Idade: {}"  .format(nome, idade))
print("Nome: {1} Idade: {0}"  .format(nome, idade))
print("Nome: {nome} Idade: {idade}"  .format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {age}"  .format(name=nome, age=idade))
print("Nome: {nome} Idade: {idade}"  .format(**dados))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:5.2f}") # Aqui no saldo o primeiro número é referente as casas que ele pula, o segundo são as casas decimais do float