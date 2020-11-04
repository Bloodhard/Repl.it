x = float(input('Digite o valor de "X": '))
y = float(input('Digite o valor de "Y": '))

print(f'X: {x}, Y: {y}')

if x != 0 and y != 0:
    if x > 0 and y > 0:
        print('Ponto ({x},{y}) esta no 1 quadrante')
    if x > 0 and y < 0:
        print('Ponto ({x},{y}) esta no 4 quadrante')
    if x < 0 and y > 0:
        print('Ponto ({x},{y}) esta no 2 quadrante')
    if x < 0 and y < 0:
        print('Ponto ({x},{y}) esta no 3 quadrante')
elif x == 0 and y != 0:
    if y > 0:
        print('Ponto ({x},{y}) esta sobre o eixo X')
        print('Entre o 1 e 2 quadrante')
    if y < 0:
        print('Ponto ({x},{y}) esta sobre o eixo X')
        print('Entre o 3 e 4 quadrante')
elif y == 0 and x != 0:
    if x > 0:
        print('Ponto ({x},{y}) esta sobre o eixo Y.')
        print('Entre o 1 e 4 quadrante')
    if x < 0:
        print('Ponto esta sobre o eixo Y.')
        print('Entre o 2 e 3 quadrante')
else:
    print('Ponto ({x},{y}) esta no centro do plano cartesiano')
