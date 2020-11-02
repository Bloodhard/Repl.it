op='n'
while op !='S' or op!='s':
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
   
  if resultado >=7:
    print('\nVocê foi aprovado com média: ',resultado)
  elif resultado < 4:
    print('\nVocê foi reprovado, sua média foi de: ',resultado)
  else:
    print('\nVocê está de exame, sua nota é de: ',resultado)
  op=input('\nSe desejar sair do programa, aperte "S", aperte qualquer outra tecla para continuar:\n ')
