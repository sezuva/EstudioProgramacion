print("Asi se muestra texto")
#asi se comenta en Python

"""
Asi se introducen
varias lineas
"""
#tipos de datos y uso

variable="Así se crean variables"
print(variable+" y así se muestran")
variablenumerica=22
print("Mostrar primero texto y despues numero:", variablenumerica)
#preguntar=input("¿así se solicita datos en python?")
#print(preguntar)
boleano=False
boleano=not False
print(boleano)
print(type(boleano))
entero=int(2)
print(type(entero))
entero=bool("")
print(type(entero))
print(entero)
uso_comillas='hola2 j1'
print(uso_comillas)

#concatenar texto y variables:
nombre="Sebastián"
apellido="Zuñiga"
union="Mi nombre es "+nombre+" y mi apellido "+apellido
print(union)
union="Mi nombre es {} y mi apellido {}".format(nombre,apellido)
print(union)
union=f"Mi nombre es {nombre} y mi apellido {apellido}"
print(union)

#abrevación en la suma
lives=1
lives+=1
print(lives)
lives+=5
print(lives)

#transformación de tipos de datos

age= 23
print("Mi edad es "+str(age))
print(f"Mi edad es {age}")

#age =input("Escribe tu edad =>")
print(type(age))
age=(int(age))
age+=10
print(f"Tu edad en 10 años será {age}")
print("Finalizado")
print("Multiplica_palabras "*3) #repite las palabras por 3 veces

#Operadores de comparación
print(3>2) #true
print(3>=2) #true
print(3==3) #IGUAL.. TRUE
print(3!=3) #diferente.. false

print("Hola" == "hola") #da false por la mayuscula...
print(type("hola")== type("holass"))#da true, porque es el mismo tipo
print((1.1+2.6))
