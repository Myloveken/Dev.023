#Conjuntos Bons e Ruins

while True:
  qtd = int(input())
  if qtd == 0:
    break

  conjunto = []

  prefixo = False
  for i in range(qtd):
    conjunto.append(input())
  conjunto.sort()

  for p in range(len(conjunto)-1):
    if ((conjunto[p].find(conjunto[p+1])==0) or(conjunto[p+1].find(conjunto[p])==0)):
      prefixo = True
      break

  if prefixo:
    print("Conjunto Ruim")

  else:
    print("Conjunto Bom")