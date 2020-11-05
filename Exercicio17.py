notas=input('Deseja utilizar quantas notas para a média?\n 1 - Para 2 notas;\n 2- Para 3 notas;\n 3- Para 4 Notas \n: ')

if notas == '1':
  n1=int(input('\nInsira a nota da N1:\n '))
  n2=int(input('\nInsira a nota da N2:\n '))
  med= n1 + n2
  result = med / 2
  print('Sua média é: ',result)
elif notas == '2':
  n1=int(input('\nInsira a nota da N1:\n '))
  n2=int(input('\nInsira a nota da N2:\n '))
  n3=int(input('\nInsira a nota da N3:\n '))
  med= n1+n2+n3
  result= med/3
  print('Sua média é: ',result)
elif notas == '3':
  n1=int(input('\nInsira a nota da N1:\n '))
  n2=int(input('\nInsira a nota da N2:\n '))
  n3=int(input('\nInsira a nota da N3:\n '))
  n4=int(input('\nInsira a nota da N4:\n '))
  med= n1+n2+n3+n4
  result= med/4
  print('Sua média é: ',result)
   
if result >=7:
  print('\nVocê foi aprovado com média: ',result)
elif result < 4:
  print('\nVocê foi reprovado, sua média foi de: ',result)
else:
  print('\nVocê está de exame, sua nota é de: ',result)
  
