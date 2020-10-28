pos=[]
neg=[]
zeros=[]
pares=[]
impares=[]


count= 0
while count <= 25:
  num =float (input('Digite um numero real qualquer: '))
  if num > 0:
    pos.append(num)
  elif num < 0:
   neg.append(num)
  elif num == 0 :
   zeros.append(num)
  if (num%2) == 0:
    pares.append(num)
  if num%2:
   impares.append(num)

  print('\n Numeros Positivos: \n',pos)  
  print('\n Numeros Negativos: \n',neg)
  print('\n Quatidade de zeros: \n',zeros)  
  print('\n Numeros pares: \n',pares)
  print('\n Numeros impares: \n',impares)  
  count +=1
