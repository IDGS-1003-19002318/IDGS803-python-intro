import os # Importamos el modulo os

print("Hello World!!!!!")

x = int(input("Introduce un numero: "))
y= int(input("Introduce otro numero: "))

def suma(a,b):
    return a+b

os.system("clear") # Limpia la pantalla
print(suma(x,y))

