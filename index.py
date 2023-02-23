import random
from funcion import validacion

class main:
  i = random.randint(1, 2)
  print(f"Comienza el jugador {i}")
  rondas = 1
  resultado = int(input("Ingresa el primer numero : "))
  while resultado < 30:
    numero = int(input("Ingresa el numero : "))
  
    if numero >= 1 and numero <= 3:
      resultado += numero
      print(f"resultado = {resultado}")
      rondas +=1
    
    else:
      print("ERROR! ingresa el numero de nuevo")
  
  ganador = validacion(rondas)
    
  if ganador != 0:
    print(f"Felicitaciones!, ganaste jugador numero {i}")

  else:
    print(f"Felicitaciones!, ganaste otro jugador")

  print(f"Rondas jugadas : {rondas}")

