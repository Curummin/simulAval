import random

dados = []

for _ in range (90) :
        dados.append(random.randint(40,80))

for _ in range (5) :
        dados.append(random.randint(0,10))

for _ in range (5) :
        dados.append(random.randint(90,120))

random.shuffle(dados)
with open ("./lab01/dados.txt","w") as arq:
        for valor in dados :
                arq.write (f"{valor}\n")

print("Arquivo gerado com ",len (dados)," valores.")