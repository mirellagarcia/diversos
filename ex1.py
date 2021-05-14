#1.	Você tem uma lista de número: [6,7,4,7,8,4,2,5,7,'hum', 'dois']. A ideia do exercício é tirar a média de todos os valores contidos na lista, porém para fazer o cálculo precisa remover as strings.

print("Bem-vindo")
#Exercicio 1

total = 0
index = 0
x = [6,7,4,7,8,4,2,5,7,'hum', 'dois']
for valor in x:
  if type(valor) == int:
    index = index + 1
    total = total + valor
  else:
    continue
print(total/index)
