while True:
    num = int(input('Digite um numero entre 2 e 20: '))
    if 2 < num < 20:
        break
    pass

numeros = ''
for numero in range(1, num+1):
    numeros += str(numero)
print(numeros)

novo = ''
cont = len(numeros) - 1
for numero in range(1, len(numeros)):
    novo = 'x' * numero + numeros[0:cont]
    cont -= 1
    print(novo)
