"""
     @autor: joseloordoñez
     nombre:ejercicio6.py
     descripcion:...
     Joselo Ordoñez --35
"""


nombre = input("Ingrese su nombre:")
edad =input("ingrese su edad: \n")
nota1 =input("ingrese el valor de su nota 1")
nota2 = input("ingrse el valor de su nota 2")

suma = int(nota1) + int(nota2);
promedio = suma / 2
print("%s --%s\nSu suma de notas es %s\nSu promedio es %s"%
      (nombre, edad, suma, promedio))
