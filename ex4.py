#4. Crie uma matriz nxn (n=5). Agora some essa matriz com a matriz do exercício 3.

print("Bem-vindo")
#Exercicio 4

import numpy as np
a = np.array([(5,5,5,4,3,2,1), (6,7,8,9,1,2,3), (6,5,4,3,2,1,9), (5,4,3,2,1,9,8), (3,3,3,4,3,2,1)])
print(a)

print(" ")

b = np.array([(5,5,5,4,3), (6,7,8,9,1), (6,5,4,3,2), (5,4,3,2,1), (3,3,3,4,3)])
print(b)

#Soma das Matrizes
print("Não é possivel somar duas matrizes de tamanho diferente")
