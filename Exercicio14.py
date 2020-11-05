l_e = []
list1 = []
while True:
    list1.append(input('Digite o nome: '))
    list1.append(input('Digite o salario: '))
    l_e.append(list1)
    list1 = []
    test = input('Digite "sair" caso deseje parar: ')
    if test == 'sair':
        break
    else:
        pass

print(f'\n{l_e}\n')
for nome, salario in l_e:
    sn= salario
    print('Salario bruto de {nome}: {float(salario)}')
    if float(salario) <= 1045.00:
        sn= float(salario) - float(salario) * 0.075
        print('Salario de {nome} apos INSS: {sn}')
    if 1045.01 <= float(salario) <= 2089.60:
        sn= float(salario) - float(salario) * 0.09
        print('Salario de {nome} apos INSS: {sn}')
    if 2089.61 <= float(salario) <= 3134.40:
        sn= float(salario) - float(salario) * 0.12
        print('Salario de {nome} apos INSS: {sn}')
    if float(salario) > 3134.40:
        sn= float(salario) - float(salario) * 0.14
        print('Salario de {nome} apos INSS: {sn}')

    if float(salario) <= 1903.98:
        sn= float(sn) - float(salario) * 0
        print('Salario de {nome} apos INSS e IR: {sn}')
    if 1903.99 <= float(salario) <= 2826.65:
        sn= float(sn) - float(salario) * 0.075
        print('Salario de {nome} apos INSS e IR: {sn}')
    if 2826.66 <= float(salario) <= 3751.05:
        sn= float(sn) - float(salario) * 0.15
        print('Salario de {nome} apos INSS e IR: {sn}')
    if 3751.06 <= float(salario) <= 4664.68:
        sn= float(sn) - float(salario) * 0.225
        print('Salario de {nome} apos INSS e IR: {sn}')
    if float(salario) > 4664.68:
        sn= float(sn) - float(salario) * 0.275
        print('Salario de {nome} apos INSS e IR: {sn}')
    print()
