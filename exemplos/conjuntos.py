import  matplotlib.pyplot as plt
import numpy as np
from matplotlib_venn  import  venn2

# Definição do espaço amostral e dos eventos como conjuntos
espaco_amostral = {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
A = {1 , 2 , 3 , 4}
B = {3 , 4 , 5 , 6}

# Operaçes entre eventos
uniao = A | B # União de A com B

intersecao = A & B # Interseção de A e B
complemento_A = espaco_amostral - A # Complementar de A
complemento_B = espaco_amostral - B # Complementar de B
# Exibição dos resultados
print (f" Espaço amostral : { espaco_amostral } " )
print (f" Evento A : { A } " )
print (f" Evento B : { B } " )
print (f" União dos eventos ( A e B ) : { uniao } " )
print (f" Interseção dos eventos ( A e B ) : { intersecao } " )
print (f" Complemento de A ( A ^ c ) : { complemento_A } " )
print (f" Complemento de B ( B ^ c ) : { complemento_B } " )
# Visualização com Diagrama de Venn
plt . figure ( figsize =(4 , 4) )

venn2 ([ A , B ] , ( 'Evento A ' , 'Evento B') )
plt . title ("Diagrama de Venn : Operaçõe entre eventos")
plt.show()