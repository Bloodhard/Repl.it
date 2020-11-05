lista = []
for x in range(30):
  lista.append(input("digite o número desejado "))
print('A sua lista de numeros é: ')
print(lista, '\n')

listaI = []
listaP =[]
for x in range(len(lista)+1):
  if x != 0:
    if (x % 2) == 0:
      listaP.append(x)
    else: 
      listaI.append(x)

print('os números impares são:')
print(listaI)

print('os números pares são:')
print(listaP)
