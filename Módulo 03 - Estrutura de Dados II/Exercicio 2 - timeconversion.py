def timeConversion(s):
    # Write your code here
    lista = s.split(':')
    hora = (lista[0])
    minutos = (lista[1])
    segundos = (lista[2])

    dicionario_convert = {"01":13,"02":14,"03":15,"04":16,"05":17,"06":18,"07":19,"08":20,"09":21,"10":22,"11":23,"12":00}
    valor = dicionario_convert[hora]
    print(f'{valor}:{minutos}:{segundos}')

timeConversion("07:05:45PM")