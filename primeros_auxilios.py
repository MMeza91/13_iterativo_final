print("\nHola, Este programa está diseñado para ayudarte ante una emergencia:\n")

adentro=True
while adentro:

    continuar=True
    pregunta=True
    while pregunta:    
        valor=input("\n¿La persona responde a estimulos? (Si/No): ")
        if (valor.lower()=="si" or valor.lower()=="s"):
            pregunta=False
            print("\nValorar la necesidad de llevarlo al Hospital más cercano\n")
            continuar=False
        elif (valor.lower()=="no" or valor.lower()=="n"):
            pregunta=False
            print("\nAbrir la Vía Aérea")
            continuar=True
        else:
            print("\nValor no válido")



    pregunta=True
    while pregunta and continuar:    
        valor=input("\n¿La persona respira? (Si/No): ")
        if (valor.lower()=="si" or valor.lower()=="s"):
            pregunta=False
            print("\nPermitirle posición de suficiente ventilación!\n")
            continuar=False
        elif (valor.lower()=="no" or valor.lower()=="n"):
            pregunta=False
            print("\nAdministrar 5 ventilaciones y llamar a ambulancia")
            continuar=True
        else:
            print("\nValor no válido")

    sin_ambulancia=True
    while sin_ambulancia and continuar:
      pregunta=True
      while pregunta:    
          valor=input("\n¿Tiene signos de vida? (Si/No): ")
          if (valor.lower()=="si" or valor.lower()=="s"):
              pregunta=False
              print("\nContinuar con la espera de la ambulancia!\n")
          elif (valor.lower()=="no" or valor.lower()=="n"):
              pregunta=False
              print("\nAdministrar compresiones toráxicas hasta que llegue la ambulancia")
          else:
              print("\nValor no válido")

      pregunta=True
      while pregunta:    
          valor=input("\n¿Llegó la ambulancia? (Si/No): ")
          if (valor.lower()=="si" or valor.lower()=="s"):
              pregunta=False
              sin_ambulancia=False
              continuar=False
          elif (valor.lower()=="no" or valor.lower()=="n"):
              pregunta=False
              sin_ambulancia=True
              
          else:
              print("\nValor no válido")
    
    print("\nLo siguiente no está en tus manos\n")
    pregunta=True
    while pregunta:    
        valor=input("\n¿Quieres analizar otra instancia de emergencia? (Si/No): ")
        if (valor.lower()=="si" or valor.lower()=="s"):
            pregunta=False
        elif (valor.lower()=="no" or valor.lower()=="n"):
            pregunta=False
            adentro=False
            print("\nNos vemos en una proxima ocasión")
        else:
            print("\nValor no válido")