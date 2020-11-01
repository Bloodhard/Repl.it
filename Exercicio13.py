def cargos():
  if idade >= 15 and idade <=17:
    menor.append(nome)
  return

def maiores():
  if idade >= 21:
   maior.append(nome)
  return

def sala():
  if salario >= 1500 and salario <= 2000:
    sal.append(salario)
    return

def dinheirao():
  if salario >= 3500:
     money.append(salario) 
     return

menor=[]
maior=[]
sal=[]
money=[]


op='N'
while op!='S' and op!='s':

  nome = input('Insira um nome: ')
  idade = int(input('Insira a idade: '))
  salario = float(input('Insira o salario: '))
  cargos()
  maiores()
  sala()
  dinheirao()
  print('\nOs menores de idade (15 ~ 17) são: ''\n', menor)
  print('\nOs maiores de idade (21+) são: ''\n', maior)
  print('\n Os com baixa renda (1500 ~ 2000) tem: ''\n',sal)
  print('\n Os com melhor renda (3500+) tem um salario de: ''\n',money)

  op=input('\nPara sair do programa digite' 'S: ')
[03:33]
Da pra ficar mto melhor em questão estetica
[03:33]
mas o código ta funcionando
