import sys

ventas={"Enero":15000,
        "Febrero":22000,
        "Marzo":12000,
        "Abril":17000,
        "Mayo":81000,
        "junio":13000,
        "Julio":21000,
        "Agosto":41200,
        "Septiembre":25000,
        "Octubre":21500,
        "Noviembre":91000,
        "Diciembre":21000,
        }
  
print("\nHola, Este programa está diseñado para entregar los valores de venta mayores al entregado:\n")

adentro=True
while adentro:
    invalido=True
    while invalido:
        try:
            if len(sys.argv) > 1:
                valor=int(sys.argv[1])
                print(f"\nEl valor de venta solicitado es: {valor:.1f}")
            else:
                vealor=int(input("\nTamaño de venta a analizar en pesos: "))
            invalido=False
       
        except ValueError:
            invalido=True
            sys.argv=[]
            print("\n\nDebe ingresar valores numéricos enteros\n\n")
        except:
            invalido=True
            sys.argv=[]
            continue;
    lista_aciertos=[]
    for mes in ventas:
      if valor<ventas[mes]:
        lista_aciertos.append((mes,ventas[mes]))

    resultados=dict(lista_aciertos)
    print(resultados)


    pregunta=True
    while pregunta:    
        valor=input("\n¿Quieres buscar otro valor? (Si/No): ")
        if (valor.lower()=="si" or valor.lower()=="s"):
            pregunta=False
        elif (valor.lower()=="no" or valor.lower()=="n"):
            pregunta=False
            adentro=False
            print("\nNos vemos en una proxima ocasión")
        else:
            print("\nValor no válido")