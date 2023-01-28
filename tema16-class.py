#Herencia
class padre():
     x = 1

class operasbas(padre):
     #definir propiedades de la clase
     #global x #funciona como variable global
     num1 = 0
     num2 = 0
     res = 0

     #definir constructor de la clase
     #def __init__(self) -> None:
     #     pass

     #definir metodos de la clase
     def suma(self,a,b):
          self.num1 = a
          self.num2 = b
          return a + b

