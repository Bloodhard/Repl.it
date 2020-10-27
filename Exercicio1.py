numero = int(input('Digite um numero:'))
divisores = 0
cont = int(input('Até: '))
while cont >= numero:
  for divisor in range(1, numero):
      if numero % divisor == 0:
          divisores = divisores + 1
          if divisores > 1:
            break
  if divisores > 1:
    print(numero,'não é primo')
  elif numero == 1:
    print(numero,'não é primo')
  else:
    print(numero,'é primo')
  divisores = 0
  numero = numero + 1  