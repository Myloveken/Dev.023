#Numero Primo

N = int(input())

for repeticao in range (N):
    x = int(input())
    contador = 0
    for divisor in range(1, x +1):
        if x % divisor == 0:
            contador = contador + 1
            if contador == 2:
                print(x, "ah primo")
            else:
                print(x,"nao eh primo")