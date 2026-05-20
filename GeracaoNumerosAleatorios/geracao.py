# %% [markdown]
# **Geração de Números Aleatórios em Python**
# 
# João Gabriel Miguêz da Silva - 2023008890
# Felipe Bastos Vargas - 2023008881
# 
# # Introdução
# 
# Este trabalho tem como objetivo testar de diferentes modelos de distribuição para dados gerados aleatóriamente
# 
# Dentre as distribuições discretas serão aplicadas:
# 
# 1. **Uniforme Discreta**
# 2. **Bernoulli**
# 3. **Binomial**
# 4. **Poisson**
# 
# Já as distribuições continuas serão:
# 
# 1. **Uniforme contínua**
# 2. **Normal**
# 3. **Exponencial**
# 4. **Gama**
# 5. **Beta**
# 6. **t-Student**

# %% [markdown]
# # Metodologia
# 
# Inicialmente geramos aleatóriamente conjunto de dados usando a semente aleatória 42 para cada distribuição.  

# %%
import numpy as np
from scipy . stats import t
import pandas as pd
import math

np.random.seed (42)

# Distribuicoes discretas
ddsUniformeDiscreta = np.random.randint(0,10,size=1000)         #uniforme discreta
ddsBernoulli = np.random.binomial(n =1,p =0.5,size =1000)       #Bernoulli
ddsBinomial = np.random.binomial(n =10,p =0.5,size =1000)       #Binomial
ddsPoisson = np.random.poisson(lam=5,size =1000)                #Poisson


# Distribuicoes continuas
ddsUniformeContinua = np.random.uniform(0,1,size =1000)            #uniforme continua
ddsNormal = np.random.normal(0,1,size =1000)                       #normal
ddsExponencial = np.random.exponential(scale =2,size =1000)         #exponencial
ddsGamma = np.random.gamma(shape =2,scale =2,size =1000)           #gama
ddsBeta = np.random.beta( a =2,b =5,size =1000)                        #beta
ddsTStudent= t.rvs(df =5,size =1000)                                   # t-Student
 

# %% [markdown]
# Em seguida analisamos as frequências observadas dos dados de cada conjunto. Para o conjunto de dados discretos, criamos um dicionário para que fosse possível contabilizar a frequência através de um loop.

# %% [markdown]
# ## Frequencias observadas dados discretos

# %%
#Frequencias dos dados Discretos 
frqObservadaUniformeDiscreta = {}
frqObservadaBernoulli = {}
frqObservadaBinomial = {}
frqObservadaPoisson = {}

conjuntoDeDadosDiscretos = [(ddsUniformeDiscreta, frqObservadaUniformeDiscreta), 
                            (ddsBernoulli, frqObservadaBernoulli),
                              (ddsBinomial, frqObservadaBinomial), 
                              (ddsPoisson,frqObservadaPoisson)]

for dados,frq in conjuntoDeDadosDiscretos:
        for valor in dados:
                if valor in frq:
                        frq[valor] += 1  
                else:
                        frq[valor] = 1


# %% [markdown]
# ## Frequencias observadas dados continuos

# %%
NUM_BINS = 10

def contar_frequencias_continuas(dados, num_bins=NUM_BINS):
    contagens, arestas = np.histogram(dados, bins=num_bins)
    pontos_medios = (arestas[:-1] + arestas[1:]) / 2
    frq = dict(zip(pontos_medios, contagens))
    return frq, arestas

frqObservadaUniformeContinua,arestasUniformeContinua = contar_frequencias_continuas(ddsUniformeContinua)
frqObservadaNormal,arestasNormal=contar_frequencias_continuas(ddsNormal)
frqObservadaExponencial,arestasExponencial= contar_frequencias_continuas(ddsExponencial)
frqObservadaGamma,arestasGamma=contar_frequencias_continuas(ddsGamma)
frqObservadaBeta,arestasBeta=contar_frequencias_continuas(ddsBeta)
frqObservadaTStudent,arestasTStudent=contar_frequencias_continuas(ddsTStudent)


# %% [markdown]
# ## Cálculo das frequências esperadas nas distribuições

# %% [markdown]
# ### Distribuição Uniforme Discreta

# %%
n = 10          # número de valores possíveis
a = 0           # valor mínimo
b = a + n - 1   # valor máximo possível (0 + 10 - 1 = 9)

def FMP_DiscretaUniforme(n, a, b):
    
    valores_x = [i for i in range(a, b + 1)]
    probabilidade = 1 / n
    probabilidades = [probabilidade for _ in range(n)]
    fmp_resultado = dict(zip(valores_x, probabilidades))
    
    return fmp_resultado

def calcular_estatisticas_uniforme(a, b):
    esperanca = (a + b) / 2
    variancia = ((b - a + 1)**2 - 1) / 12    
    return esperanca, variancia


fmpDiscretaUniforme = FMP_DiscretaUniforme(n, a, b)
mediaTeoricaDiscUni, varTeoricaDiscUni = calcular_estatisticas_uniforme(a, b)


# %% [markdown]
# ###      Distribuição de Bernoulli

# %%
pSucesso = 0.5          
pFracasso = 1 - pSucesso

def FMP_Bernoulli(p):

    valores_x = [0, 1]
    probabilidades = [1 - p, p]
    fmp_resultado = dict(zip(valores_x, probabilidades))
    return fmp_resultado

def calcular_estatisticas_bernoulli(p):
    esperanca = p
    variancia = p * (1 - p)
    return esperanca, variancia

fmpBernoulli = FMP_Bernoulli(pSucesso)
mediaTeoricaBernoulli, varTeoricaBernoulli = calcular_estatisticas_bernoulli(pSucesso)


# %% [markdown]
# ### Distribuição Binomial

# %%
n = 10   # Número de tentativas independentes
p = 0.5  # Probabilidade de sucesso em cada tentativa

def FMP_Binomial(n, p):
    fmp_resultado = {}
    for k in range(n + 1):
        coeficiente = math.comb(n, k)                               # coeficiente binomial: n! / (k! * (n - k)!)
        probabilidade = coeficiente * (p**k) * ((1 - p)**(n - k))   #P(X = k) = Coeficiente * p^k * (1-p)^(n-k)
        # Guardar no dicionário
        fmp_resultado[k] = probabilidade
    return fmp_resultado


def calcular_estatisticas_binomial(n, p):
    esperanca = n * p
    variancia = n * p * (1 - p)
    return esperanca, variancia

fmpBinomial = FMP_Binomial(n, p)
mediaTeoricaBinomial, varTeoricaBinomial = calcular_estatisticas_binomial(n, p)

# %% [markdown]
# ### Distribuição Poisson

# %%
lam = 5  # Lambda

def FMP_Poisson(lam, limite_max=15):
    fmp_resultado = {}
    for k in range(limite_max + 1):

        fatorial_k = math.factorial(k)
        probabilidade = (math.exp(-lam) * (lam**k)) / fatorial_k    #P(X = k) = (e^(-λ) * λ^k) / k!
    
        # Guardar no dicionário
        fmp_resultado[k] = probabilidade
    return fmp_resultado

def calcular_estatisticas_poisson(lam):
    return  lam, lam

fpmPoisson = FMP_Poisson(lam)
mediaTeoriaPoisson, varTeoricaPoisson = calcular_estatisticas_poisson(lam)

# %% [markdown]
# ### Distribuição Uniforme Continua

# %%
NUM_BINS = 10
N_AMOSTRAS = 1000

def fdp_uniforme_continua(x, a=0, b=1):
    return 1 / (b - a) if a <= x <= b else 0.0


# %% [markdown]
# ### Distribuição Normal

# %%
def fdp_normal(x, mu=0, sigma=1):
    termo1 = 1 / (sigma * math.sqrt(2 * math.pi))
    termo2 = math.exp(-((x - mu) ** 2) / (2 * (sigma ** 2)))
    return termo1 * termo2



# %% [markdown]
# ### Distribuição Exponencial 

# %%
def fdp_exponencial(x, lamb=0.5):
    return lamb * math.exp(-lamb * x) if x >= 0 else 0.0



# %% [markdown]
# ### Distribuição Gamma

# %%
def fdp_gamma(x, alpha=2, beta=1):
    if x < 0:
        return 0.0
    gamma_alpha = math.factorial(int(alpha) - 1) 
    termo1 = (beta ** alpha) / gamma_alpha
    termo2 = (x ** (alpha - 1)) * math.exp(-beta * x)
    return termo1 * termo2



# %% [markdown]
# ### Distribuição Beta

# %%
def fdp_beta(x, alpha=2, beta=5):

    if not (0 <= x <= 1):
        return 0.0
    num_b = math.factorial(int(alpha) - 1) * math.factorial(int(beta) - 1)
    den_b = math.factorial(int(alpha + beta) - 1)
    funcao_B = num_b / den_b
    
    return (x ** (alpha - 1)) * ((1 - x) ** (beta - 1)) / funcao_B



# %% [markdown]
# ### Distribuição t-Student

# %%
def fdp_t_student(x, df=5):
    v = df
    gamma_num = math.factorial(int((v + 1) / 2) - 1)
    gamma_den = 0.75 * math.sqrt(math.pi)
    termo_constante = gamma_num / (math.sqrt(v * math.pi) * gamma_den)
    termo_variavel = (1 + (x ** 2) / v) ** (-(v + 1) / 2)
    return termo_constante * termo_variavel

# %% [markdown]
# # Analise dos Resultados

# %%
tabelas_frequencia = [
    ("Uniforme Discreta", frqObservadaUniformeDiscreta, fmpDiscretaUniforme),
    ("Bernoulli", frqObservadaBernoulli, fmpBernoulli),
    ("Binomial", frqObservadaBinomial, fmpBinomial),
    ("Poisson", frqObservadaPoisson, fpmPoisson)
]

for nome, frq_dict, fmp_dict in tabelas_frequencia:
    print(f"\n" + "="*70)
    print(f" TABELA COMPARATIVA: {nome.upper()} ")
    print("="*70)
    
    
    df = pd.DataFrame(list(frq_dict.items()), columns=['Valor', 'Freq. Obs. Absoluta (f_o)'])
    df = df.sort_values(by='Valor').reset_index(drop=True)
    
    total_observacoes = df['Freq. Obs. Absoluta (f_o)'].sum()
    
    df['Prob. Teórica P(X=x)'] = df['Valor'].map(fmp_dict)
    df['Prob. Teórica P(X=x)'] = df['Prob. Teórica P(X=x)'].fillna(0)
    df['Freq. Esp. Absoluta (f_e)'] = df['Prob. Teórica P(X=x)'] * total_observacoes
    df['Freq. Obs. Relativa (f_r)'] = df['Freq. Obs. Absoluta (f_o)'] / total_observacoes
    

    df_formatado = df.copy()
    
    df_formatado['Freq. Esp. Absoluta (f_e)'] = df_formatado['Freq. Esp. Absoluta (f_e)'].map("{:.1f}".format)
    df_formatado['Prob. Teórica P(X=x)'] = df_formatado['Prob. Teórica P(X=x)'].map("{:.2%}".format)
    df_formatado['Freq. Obs. Relativa (f_r)'] = df_formatado['Freq. Obs. Relativa (f_r)'].map("{:.2%}".format)
    
    colunas_ordenadas = [
        'Valor', 
        'Freq. Obs. Absoluta (f_o)', 'Freq. Esp. Absoluta (f_e)', 
        'Freq. Obs. Relativa (f_r)', 'Prob. Teórica P(X=x)'
    ]
    print(df_formatado[colunas_ordenadas].to_string(index=False))

conjuntoDeDadosContinuos = [
        ("Uniforme Contínua",ddsUniformeContinua,frqObservadaUniformeContinua,arestasUniformeContinua),
        ("Normal", ddsNormal,frqObservadaNormal,arestasNormal),
        ("Exponencial",ddsExponencial,frqObservadaExponencial,arestasExponencial),
        ("Gama",ddsGamma,frqObservadaGamma,arestasGamma),
        ("Beta",ddsBeta,frqObservadaBeta,arestasBeta),
        ("t-Student",ddsTStudent,frqObservadaTStudent,arestasTStudent),
]

for nome, _, frq, arestas in conjuntoDeDadosContinuos:
    print(f"\n{'='*60}")
    print(f" FREQUÊNCIAS OBSERVADAS — {nome.upper()}")
    print(f"{'='*60}")
    print(f" {'Intervalo':>22}  {'Ponto Médio':>12}  {'Freq. Obs.':>10}")
    for (pmed, freq), (inf, sup) in zip(frq.items(), zip(arestas[:-1], arestas[1:])):
        print(f" [{inf:>9.4f}, {sup:>9.4f})  {pmed:>12.4f}  {freq:>10d}")


