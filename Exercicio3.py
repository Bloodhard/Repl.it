list1 = []
numrange = 30
for i in range(numrange):
  list1.append(input(f"digite o número desejado na posição {i+1}: "))
print('\nLista de Numeros: ')
print(list1, '\n')

listimp = []
listpar =[]
for i in range(len(list1)+1):
  if i != 0:
    if (i % 2) == 0:
      listpar.append(i)
    else: 
      listimp.append(i)

print('os números impares são:')
print(listimp)

print('os números pares são:')
print(listpar)
