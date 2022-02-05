def staircase(n):
    # Write your code here
    cont = 1
    lista = []

    while cont <= n:
        a = (n-cont) * " "
        b = "#" * cont
        c = a + b
        lista.append(c)
        cont = cont + 1

    for i in lista:
        print(i)

staircase(4)
