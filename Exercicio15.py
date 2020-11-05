n1=float(input('Digite o Primeiro número: '))
n2=float(input('Digite o Segundo número: '))

for i in range(120):
  print('=', end = '')

print(f'\n1 - Soma / 2 - Subtração/ 3 - multiplicação/ 4 - divisão/ 5 - verificar se {int(n1)} é menor que {int(n2)}/ 6 - verificar se {n1} é maior que {n2} ')
op=input('Digite a operação desejada: ')
if op == '1':
  print(n1+n2)
elif op == '2':
  print(n1-n2)
elif op == '3':
  print(n1*n2)
elif op == '4':
  print(n1/n2)
elif op == '5':
  n1 < n2
  print(n2)
elif op == '6':
  n1 > n2
  print(n1)


