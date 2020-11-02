op = 'N'
while op != 'S' or op != 's':
  mon=float(input('Digite o valor em dinheiro que gostaria de converter:\n '))
  con=input('Selecione o método de conversão desejado:\n 1= Real para dolar;\n 2= Real para euro;\n 3= Dolar para Real;\n 4= Dolar para euro;\n 5= Euro para Real;\n 6= Euro para Dolar;\n')

  if con == '1':
    mon = mon*5.74
    print('A Conversão de Real para Dolar ficou:\n',mon)
  if con == '2':
    mon = mon*6.71
    print('A conversão de Real para Euro ficou:\n ',mon)
  if con == '3':
    mon= mon*0.17
    print('A conversão de Dolar para Real ficou:\n',mon )
  if con == '4':
    mon= mon*0.86
    print('A conversão de Dolar para Euro ficou:\n ',mon)
  if con == '5':
    mon= mon*0.15
    print('A Conversão de Euro para Real ficou:\n',mon)
  if con == '6':
    mon= mon*1.17
    print('A Conversão de Euro para Dolar ficou:\n',mon)
  op=input('Para sair do programa digite "S", Para reutilizar o programa, digite "n":\n')
