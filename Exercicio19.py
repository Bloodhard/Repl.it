from random import randint

listaDeCorredores = {
  'Renan': [],
  'Marcos': [],
  'Usain': [],
  'Camila': [],
  'Sasuke': [],
  'Baraka': []
}

melhorVolta = 100
corredorMelhorVolta = ''
numeroDaVolta = 0
melhorMedia = 100
melhorCorredor = ''

for corredor in listaDeCorredores:
  total = 0
  for i in range(10):
    tempo = randint(40,60)
    if tempo <= melhorVolta:
      melhorVolta = tempo
      corredorMelhorVolta = corredor
      numeroDaVolta = i+1
    listaDeCorredores[corredor].append(tempo)
    total += tempo 
  print(corredor, listaDeCorredores[corredor])
  media = total/10
  listaDeCorredores[corredor].append(media)



print(corredorMelhorVolta, melhorVolta, numeroDaVolta)
for corredor in listaDeCorredores:
  print(listaDeCorredores[corredor][10])

print(listaDeCorredores)
