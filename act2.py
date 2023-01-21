def suma(x,y):
     print("{} + {} = {}".format(x,y,(x+y)))

def resta(x,y):
     print("{} - {} = {}".format(x,y,(x-y)))


def multiplicacion(x,y):
     print("{} x {} = {}".format(x,y,(x*y)))

def dividir(x,y):
     print("{} / {} = {}".format(x,y,(x/y)))
          
def main():
     opcion = int(
     input("Ingresa la operacion a relizar \n1 - Suma \n2 - Resta\n3 - Multiplicacion\n4 - Division\n5 - Salir \n :")
     )
     num1 = int(input("Ingresa un numero: "))
     num2 = int(input("Ingresa otro numero: "))
     while (opcion != 5):
          if opcion == 1:
               suma(num1,num2)
          elif opcion == 2:
               resta(num1,num2)
          elif opcion == 3:
               multiplicacion(num1,num2)
          elif opcion == 4:
               dividir(num1,num2)
          else:
               print("Adios bye")
          opcion = int(
          input("Ingresa la operacion a relizar \n1 - Suma \n2 - Resta\n3 - Multiplicacion\n4 - Division\n5 - Salir \n :")
          )

if __name__=="__main__":
     main()