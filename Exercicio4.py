def convert(numero):
  nR = listaR[numero - 1]
  return(nR)

listaR = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI','XXII','XXIII','XXIV','XXV','XXVI','XXVII','XVIII','XXIX','XXX','XXXI','XXXII','XXXIII','XXXIV','XXXV','XXXVI','XXXVII','XXXVIII','XXXIX','XL','XLI','XLII','XLIII','XLIV','XLV','XLVI','XLVII','XLVIII','XLIX','L']


numero = int(input('digite o numero desejado '))
validador = True
while validador == True:
  if (numero > 50) or (numero <= 0):
    print('Numero invalido')
    validador = True
  else:
    validador = False
numeroRomano = convert(numero)

print('numero em romano é ', numeroRomano)
