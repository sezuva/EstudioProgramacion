print("Asi se muestra texto")
#asi se comenta en Python

"""
Asi se introducen
varias lineas

operadores:

+ suma
- resta
* multiplicacion
/ division
% residuo
// division con valor entero
** exponenciación
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
print(3.3==(1.1+2.2)) #da false por error de punto flotante, ver aritmetica de punto flotante
print(format(1.1+2.2,".2g"))

#Operadores logicos and y or

print(True and  True) #true
print(False and False) #false
print(False and True) #false
print(False or True) #true

#Operador not

print(not True) #False

#If o condicionales

if True:
    print("Escribir")
"""
edad=abs(float(input("¿Cuantos años tienes?")))

if edad >= 0 and edad <=20:
    print("Eres joven")
elif edad > 20 and edad <=60:
    print("Eres adulto")
else:
    print("Estas viejo")"""

#Operador in y len
text = "Ella sabe programar en Python"
print("Ultimos cambios")
print("Hola" in text) # da false porque "Hola" no está en la oración
print("Python" in text) #da verdadero porque el operador in busca la palabra "Python" en la oración anterior
size=len(text) #cuenta el numero de caracteres que tiene el texto
print(size)
print(text.upper()) #transforma a MAYUSCULA
print(text.lower()) #transforma a minuscula
print(text.count('a')) #cuenta las "a" del texto
print(text.swapcase()) #canbia las mayusculas por minusculas y viceversa
print(text.startswith("Ella")) #Evalua si es la primera palabra.
print(text.endswith("Rust")) #Evalua si termina en la palabra indicada "rust"
print(text.replace("Ella", "YO")) # Reemplaza en el texto "Ella" por "YO"
print(text.capitalize()) #Coloca la primera letra en mayuscula
print(text.title()) #coloca cada primera letra de cada palabra en mayuscula.
print(text.isdigit()) #evalua si es un dígito.

#--------------- Indexing and slicing
text="Ella sabe Python"
print(text[0]) #da E, porque es el caracter en posición 0
print(text[-1]) #da n, porque empieza de derecha a izquierda en la posición -1 (negativa)
print(text[0:3]) # Da ella, porque toma las posiciones del 0 al 10

#----------listas
numbers = [1,2,3,4]
print(numbers)
print(type(numbers))
