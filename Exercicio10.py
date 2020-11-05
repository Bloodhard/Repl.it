vet1 = []
vet2 = []
print('entre com os valores do vetor 1:\n')
for i in range(10):
vet1.append(input(f'Entre com o valor da linha {i+1}: '))
print('\nentre com os valores do vetor 2:')
for l in range(10):
vet2.append(input(f'Entre com o valor da linha {l+1}: '))
print(vet1)
print(vet2)

som = []
cont = 0
cont2 = len(vet2)-1
	
for n in vet1:
som.append(int(vet1[cont]) + int(vet2[cont2]))
cont += 1
cont2 -= 1
print(f'A soma dos termos dos vetores são:{som}')
