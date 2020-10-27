from random import choice

vogais = [1, 3, 5]

consoantes = [0, 2, 4]

nomes = ['Kisame', 'Jiraya', 'Hinata', 'Renata', 'Madara', 'Jaqueli', 'Marisa', 'Zabuza', 'Gogeta', 'Yosuke', 'Josuke', 'Jotaro', 'Josefe', 'Hanabi', 'Julyne', 'Jonatã']

validador = True

while validador == True:
  nome1 = choice(nomes)
  nome2 = choice(nomes)
  while nome1 == nome2:
    nome2 = choice(nomes)
  print(nome1)
  print(nome2, '\n')
  tipo = True

  for x in range(3):
    while tipo == True:
      letrav = nome1[choice(vogais)]
      letra2v = nome2[choice(vogais)]
      while letrav == letra2v:
        letra2 = nome2[choice(vogais)]
      
      letrac = nome1[choice(consoantes)]
      letra2c = nome2[choice(consoantes)]
      while letrac == letra2c:
        letra2 = nome2[choice(consoantes)]
      
      print('\n',letrav, letra2v)
      nome3v = nome1.replace(letrav, letra2v)
      nome3v2 = nome2.replace(letra2v, letrav)
      print(nome3v)
      print(nome3v2)  
      
      print('\n',letrac, letra2c)
      nome3c = nome1.replace(letrac, letra2c)
      nome3c2 = nome2.replace(letra2c, letrac)
      print(nome3c) 
      print(nome3c2)
    tipo = False
    