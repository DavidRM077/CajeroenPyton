

DineroActual = 1000
Entrada = 0


print("HOLA BIENVENIDO AL BANCO DAVIDSITO")
print("Selecione la Opcion Correspondiente")

print("1-Depositar")
print("2-Retirar")
print("3-Consultar")

opciones = int(input("Digite un numero"))

if opciones ==1:
    extra = int(input("Ingresa el monto a Depositar"))
    DineroActual += extra
    print("El Dinero Actual es de " + str(DineroActual))

elif opciones == 2:
       retirar = int(input("Cuanto quieres retirar")) 
       if retirar > DineroActual:
             print("No tiene esa cantidad de dinero")

       else:
         DineroActual -= retirar
       print("El Dinero Actual es de " + str(DineroActual)) 

elif opciones == 3:
      print(DineroActual)
      print("Gracias por preferirnos")      


      