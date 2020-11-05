
lista_empregados = []
lista = []
while True:
    lista.append(input('Digite o nome: '))
    lista.append(input('Digite o salario: '))
    lista_empregados.append(lista)
    lista = []
    teste = input('Digite "sair" caso deseje parar: ')
    if teste == 'sair':
        break
    else:
        pass

print(f'\n{lista_empregados}\n')
for nome, salario in lista_empregados:
    salarioNovo = salario
    print('Salario bruto de {nome}: {float(salario)}')
    if float(salario) <= 1045.00:
        salarioNovo = float(salario) - float(salario) * 0.075
        print('Salario de {nome} apos INSS: {salarioNovo}')
    if 1045.01 <= float(salario) <= 2089.60:
        salarioNovo = float(salario) - float(salario) * 0.09
        print('Salario de {nome} apos INSS: {salarioNovo}')
    if 2089.61 <= float(salario) <= 3134.40:
        salarioNovo = float(salario) - float(salario) * 0.12
        print('Salario de {nome} apos INSS: {salarioNovo}')
    if float(salario) > 3134.40:
        salarioNovo = float(salario) - float(salario) * 0.14
        print('Salario de {nome} apos INSS: {salarioNovo}')

    if float(salario) <= 1903.98:
        salarioNovo = float(salarioNovo) - float(salario) * 0
        print('Salario de {nome} apos INSS e IR: {salarioNovo}')
    if 1903.99 <= float(salario) <= 2826.65:
        salarioNovo = float(salarioNovo) - float(salario) * 0.075
        print('Salario de {nome} apos INSS e IR: {salarioNovo}')
    if 2826.66 <= float(salario) <= 3751.05:
        salarioNovo = float(salarioNovo) - float(salario) * 0.15
        print('Salario de {nome} apos INSS e IR: {salarioNovo}')
    if 3751.06 <= float(salario) <= 4664.68:
        salarioNovo = float(salarioNovo) - float(salario) * 0.225
        print('Salario de {nome} apos INSS e IR: {salarioNovo}')
    if float(salario) > 4664.68:
        salarioNovo = float(salarioNovo) - float(salario) * 0.275
        print('Salario de {nome} apos INSS e IR: {salarioNovo}')
    print()
