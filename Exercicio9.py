def calc():
  num = int(input('Entre com o numero: '))
  if num < 0 :
    print('valor negativo: ',-1)
  elif num > 0:
    print('valor positivo:',1)
  else:
    print('O valor é zero:',0)
    return calc()

calc()
