#2.	crie um método que receba duas matrizes, some os valores total de cada matriz e depois multiple o resultado delas e retorne o valor.
print("Bem-vindo")
#Exercicio 2

def matriz():

 x = [[5,5,5], [6,7,8], [6,5,4]]
 soma_x = 0
 j = 0
 for lista_x in x:
    print(lista_x)
    for j in lista_x:
      print(j)
      soma_x = soma_x + j
 print("Soma da Matriz X é de: ", soma_x)

 print("###")

 y = [[2,3,4], [5,6,7], [8,9,1]]
 soma_y = 0
 k = 0
 for lista_y in y:
    print(lista_y)
    for k in lista_y:
      print(k)
      soma_y = soma_y + k
 print("Soma da Matriz Y é de: ", soma_y)


 multiplicacao = 0
 multiplicacao = soma_x * soma_y
 print("Multiplicação das Matrizes X e Y é de: ", multiplicacao)

matriz()
