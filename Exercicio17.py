op='n'
while op !='S' and op!='s':
  notas=input('Deseja utilizar quantas notas para a média?\n 1 - Para 2 notas;\n 2- Para 3 notas;\n 3- Para 4 Notas \n: ')

  if notas == '1':
    n1=int(input('\nInsira a nota da N1:\n '))
    n2=int(input('\nInsira a nota da N2:\n '))
    media= n1 + n2
    resultado = media / 2
    print('Sua média é: ',resultado)
  elif notas == '2':
    n1=int(input('\nInsira a nota da N1:\n '))
    n2=int(input('\nInsira a nota da N2:\n '))
    n3=int(input('\nInsira a nota da N3:\n '))
    media= n1+n2+n3
    resultado= media/3
    print('Sua média é: ',resultado)
  elif notas == '3':
    n1=int(input('\nInsira a nota da N1:\n '))
    n2=int(input('\nInsira a nota da N2:\n '))
    n3=int(input('\nInsira a nota da N3:\n '))
    n4=int(input('\nInsira a nota da N4:\n '))
    media= n1+n2+n3+n4
    resultado= media/4
    print('Sua média é: ',resultado)
