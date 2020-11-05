Ent = 'N'
while Ent != 'S' or Ent != 's':
  Din=float(input('Digite o valor em dinheiro que gostaria de converter:\n '))
  con=input('Selecione o método de conversão desejado:\n 1= Real para dolar;\n 2= Real para euro;\n 3= Dolar para Real;\n 4= Dolar para euro;\n 5= Euro para Real;\n 6= Euro para Dolar;\n')

  if con == '1':
    Din = Din*5.74
    print('A conversão de Real para Dolar ficou:\n',Din)
  if con == '2':
    Din = Din*6.71
    print('A conversão de Real para Euro ficou:\n ',Din)
  if con == '3':
    Din= Din*0.17
    print('A conversão de Dolar para Real ficou:\n',Din )
  if con == '4':
    Din= Din*0.86
    print('A conversão de Dolar para Euro ficou:\n ',Din)
  if con == '5':
    Din= Din*0.15
    print('A conversão de Euro para Real ficou:\n',Din)
  if con == '6':
    Din= Din*1.17
    print('A conversão de Euro para Dolar ficou:\n',Din)
Ent=input('Para sair do programa digite "S", Para reutilizar o programa, digite "n":\n')
