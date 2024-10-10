n = int(input('Esse número pertence a Fibonacci?: '))
n1 = 0
n2 = 1

while n1 < n:
    n1, n2 = n2, n1 + n2

if n1 == n:
    print(f"{n} é um número de Fibonacci.")
else:
    print(f"{n} não é um número de Fibonacci.")