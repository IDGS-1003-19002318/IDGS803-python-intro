import os

class OperacionesBasicas:

     x = 0
     y = 0

     def suma(self,a,b):
          self.x = a
          self.y = b
          return a + b
     
     def resta(self,a,b):
          self.x = a
          self.y = b
          return a - b
     
     def multiplicacion(self,a,b):
          self.x = a
          self.y = b
          return a * b
     
     def division(self,a,b):
          self.x = a
          self.y = b
          return a / b

def main():
     os.system("clear")
     obj = OperacionesBasicas()
     print("Operaciones Basicas")
     print("")

     #op = OperacionesBasicas(x, y)
     op = int(
     input("Ingresa la operacion a relizar \n1 - Suma \n2 - Resta\n3 - Multiplicacion\n4 - Division\n5 - Salir \n :")
     )

     x = int(input("Ingrese un valor: "))
     y = int(input("Ingrese otro valor: "))
     print("")
     while (op != 5):
          if op == 1:
               print("Suma")
               print("{} + {} = {}".format(x,y,obj.suma(x,y)))
          elif op == 2:
               print("Resta")
               print("{} - {} = {}".format(x,y,obj.resta(x,y)))
          elif op == 3:
               print("Multiplicacion")
               print("{} x {} = {}".format(x,y,obj.multiplicacion(x,y)))
          elif op == 4:
               print("Division")
               print("{} / {} = {}".format(x,y,obj.division(x,y)))

          print("")
          op = int(input("Ingresa la operacion a relizar \n1 - Suma \n2 - Resta\n3 - Multiplicacion\n4 - Division\n5 - Salir \n :"))
          if op != 5:
               x = int(input("Ingrese un valor: "))
               y = int(input("Ingrese otro valor: "))
          print("")
     print("Adios bye")


if __name__ == "__main__":
     main()