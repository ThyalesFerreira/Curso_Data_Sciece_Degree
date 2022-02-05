def birthdayCakeCandles(candles):
    # Write your code here
    maior_valor = max(candles)
    lista_maiores = []
    for i in candles:
        if i == maior_valor:
            lista_maiores.append(i)

    print("Candle heights are", candles, ".The tallest candles are", maior_valor, "units, and there are",
          len(lista_maiores), "of them.")

birthdayCakeCandles([3,2,1,3])