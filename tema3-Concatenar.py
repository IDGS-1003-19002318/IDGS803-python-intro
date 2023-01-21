dato1= "hola"
dato2="mundo"

datoFinal = dato1+""+dato2
print(datoFinal)
print("El saludo es: %s %s" %(dato1,dato2))

saludo = "saludo2 {0} {1}".format(dato1,dato2)
print(saludo)

saludo = "saludo2 {1} {0}".format(dato1,dato2)

print(saludo)