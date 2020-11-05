def convert(n):
  nR = listaR[n - 1]
  return(nR)

listaR = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI','XXII','XXIII','XXIV','XXV','XXVI','XXVII','XVIII','XXIX','XXX','XXXI','XXXII','XXXIII','XXXIV','XXXV','XXXVI','XXXVII','XXXVIII','XXXIX','XL','XLI','XLII','XLIII','XLIV','XLV','XLVI','XLVII','XLVIII','XLIX','L']


n = int(input('digite o numero desejado desejado de 0 a 50:  '))
valid = True
while valid == True:
  if (n > 50) or (n <= 0):
    print('numero invalido')
    valid = True
  else:
    valid = False
nRomano = convert(n)

print(f'numero {n} em romano é ', nRomano)
