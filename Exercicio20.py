temp = [0,0,0,0,0,0,0,0,0,0]

print('---Entre com 10 temperaturas ambientes da cidade ---\n')
for l in range(len(temp)):
    temp[l] = int(input(f'Entre com a temperatura  ambiente da cidade {l+1}: '))
print('\n   Lista de temperaturas:',temp)
temp.sort()
print('\n   Lista de temperaturas em ordem crescente:',temp)


media = sum(temp) / len(temp)
print('\na média de temperatura é: ',media)

minima = min(temp)
print('\na minima de temperatura é: ',minima)

maxima = max(temp)
print('\na maxima de temperatura é: ',maxima)

dados = [maxima, minima ,media] 
dados.sort()
print('\nDados ordenados em ordem crescente: ',dados)

