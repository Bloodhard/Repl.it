#Crie um programa no qual o usuário entre com dois números e diga qual é o maior número
#Aluno: Luan Fernando Duarte Guimarães

valid = True
while valid == True:
    x = int(input('n1: '))
    y = int(input('n2: '))
    if x > y:
        print(x,'é maior do que ', y)
    elif x < y:
        print(y,'é maior do que ', x)
    else:
        print(x,'e', y, 'são iguais')
    valid = input('deseja continuar?s/n: ')
    if valid == 's':
        valid = True
    else:
        valid = False
