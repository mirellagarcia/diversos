#3.	Criar uma matriz nxm (n = 5, m =7)
#a.	faça a matriz transposta desta matriz
#b.	somar toda matrix
#c.	somar todas as colunas
#d.	somar todas as linhas.
#e.	retorne o maior valor
#f.	retorne o menor valor.

print("Bem-vindo")
#Exercicio 3

import numpy as np
a = np.array([(5,5,5,4,3,2,1), (6,7,8,9,1,2,3), (6,5,4,3,2,1,9), (5,4,3,2,1,9,8), (3,3,3,4,3,2,1)])
print(a)

#A
print("Parte A: ")
a.transpose()
#B
print("Parte B: ")
a.sum()
#C
print("Parte C: ")
a.sum(axis=0)
#D
print("Parte D: ")
a.sum(axis=1)
#E
print("Parte E: ")
a.max()
#F
print("Parte F: ")
a.min()

