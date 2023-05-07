#Soma de Subconjuntos

testes = int(input())
for teste in range(testes):
  tamanho = int(input())
  conjunto = sorted([int(n) for n in input().split(" ")])
 
  resposta = 1
 
  for numero in conjunto:
    if numero>resposta:
      break

    else:
      resposta += numero
  print(resposta)
  