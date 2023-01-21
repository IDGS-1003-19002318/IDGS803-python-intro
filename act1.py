#Leer un numero
#Crear una tabla de multiplicacion 

def tablaMultiplicar(nu):
     for x in range(1,11):
          print("{1} x {0} = {2}" .format(x, nu,(x * nu)))


num = int(input("Dame un numero para la tabla de multiplicar: "))
tablaMultiplicar(num)