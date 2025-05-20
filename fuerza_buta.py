from string import ascii_lowercase

print("\nHola, Este programa está diseñado para probar las contaseñas:\n")


adentro=True
while adentro:

  clave=input("\nIngrese una contraseña sin considerar la \'ñ\' ni caracteres especiales: ")

  print(f"\nLa contraseña ingresada es: {clave}")

  largo=len(clave)
  i=0
  e=0
  rompiendo=True
  while rompiendo:
    if e<len(clave):
      for x in ascii_lowercase:
        i+=1
        if x==clave[e]:
          break;
      e+=1
    else:
      rompiendo=False



  print(f"\nLa contraseña fue forzada en {i} intentos")
    


  pregunta=True
  while pregunta:    
      valor=input("\n¿Quieres probar con otra contraseña? (Si/No): ")
      if (valor.lower()=="si" or valor.lower()=="s"):
          pregunta=False
      elif (valor.lower()=="no" or valor.lower()=="n"):
          pregunta=False
          adentro=False
          print("\nNos vemos en una proxima ocasión")
      else:
          print("\nValor no válido")