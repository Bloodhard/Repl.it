
def soma_lista(som):
  total = 0
  for i in som:
    total= total+i
  return total


som=[]
neg=[]
resultado=0




contador=0
while contador <=50:
  num=float(input('Digite um total de 50 numeros: \n'))


  if num >=0:
    som.append(num)


  print ('\nOs numeros positivos são:\n',som )
  if num <0:
    neg.append(num)
  print('\nOs numeros negativos são:\n', neg)
  print('\nA soma dos números positivos é:\n ',soma_lista(som))

  contador+1
