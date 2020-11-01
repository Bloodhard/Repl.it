def matriz():
  matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
  for l in range(len(matriz)):
    for c in range(len(matriz)):
      matriz[l][c] = int(input(f'Entre com o valor para [{l},{c}] :'))
  print('-=' * 30)
  for l in range(len(matriz)):
    for c in range(len(matriz)):
      print(f'[{matriz[l][c]}]', end= '')
    print() 
  media = (matriz[0][0] + matriz[0][1] + matriz[0][2] + matriz[0][3] + matriz[0][4] + matriz[1][0] + matriz[1][1] + matriz[1][2] + matriz[1][3] + matriz[1][4] + matriz[2][0] + matriz[2][2] + matriz[2][3] + matriz[2][4] + matriz[3][0] + matriz[3][3] + matriz[3][4] + matriz[4][0] + matriz[4][4]) / 19
  print(media)

matriz()


