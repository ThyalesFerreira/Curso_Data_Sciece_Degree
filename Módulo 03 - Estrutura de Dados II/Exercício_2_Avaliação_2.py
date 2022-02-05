def superdigit(n, k):
    concatenar = (str(n)*k)
    lista_string = (list(concatenar))# transforma em uma lista de string
    int_lista = list(map(int, lista_string)) #transforma uma lista de string em lista de inteiros.
    soma = sum(int_lista)
    if soma < 10:
        return print(soma)
    else:
        while soma > 10:
            superdigit(soma, 1)
            break

superdigit(148, 3)