# Exercício 8

'''
lambda = tx de ocorrencia 

'''

def P_poisson(txOcorrencia,k):
  if k < 0:
    return 0
  probabilidade = (math.exp(-txOcorrencia) * (txOcorrencia**k)) / math.factorial(k)
  return probabilidade

def varPoisson(txOcorrencia):
  return txOcorrencia
def espPoisson(txOcorrencia):
  return txOcorrencia

lam = 2   #por hora

print(f"a) Probabilildade de receber 3 chamadas em uma hora: {P_poisson(lam,3)}\n")
print(f"b) Probabilidade de receber nenhuma chamada:  {P_poisson(lam,0)}")
print(f"c) Número esperado de chamdas em 3 horas: {espPoisson(3*lam)}")
