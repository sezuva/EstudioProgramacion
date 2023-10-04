import this
import random
#..CONJUNTOS
#Propiedades: Se pueden modificar. No tienen un orden. No permiten duplicados.
#CREACIÓN DE CONJUNTOS
set_countries = {"Colombia", "Mexico","Bolivia","Colombia"}
print(set_countries)
print(type(set_countries))

set_from_string = set("sebas")
print(set_from_string)

set_from_tuples = set(("abc","bcd","cad"))
print(set_from_tuples)

numbers = [6,2,3,4,4,5,1,2]
set_numbers=set(numbers)
print(set(numbers))

#MODIFICACIÓN DE CONJUNTOS

size=len(set_countries) #indica cuantos elementos hay en el conjunto
print(size)
print("Colombia" in set_countries) #da true porque Colombia si está en el conjunto

#añadir elementos al conjunto con .add
set_countries.add("Perú")
print(set_countries)

# actualizar un conjunto con varios valores (añadir)
set_countries.update({"Argentina", "Ecuador"})
print(set_countries)

#eliminar elementos del conjunto, debe ser preciso o sino da error
set_countries.remove("Argentina") #elimina a argentina
print(set_countries)

#descartar un elemento, si se equivoca no pasa nada (pero no se eliminará)
set_countries.discard("Argentssa")
print(set_countries)
set_countries.add("Argentina")

#eliminar todos los elementos de un conjunto
set_countries.clear() #elimina todos los elementos del conjunto
print(set_countries)

#OPERACIONES ENTRE CONJUNTOS
#union
set_a = {"col", "mex", "bol"}
set_b = {"pe", "bol"}
set_c = set_a.union(set_b) #forma 1 para unir
print(set_c)
print(set_a | set_b) #forma 2 para unir

#intersección
set_c = set_a.intersection(set_b) #forma 1
print(set_c)
print(set_a & set_b) # forma 2

#diferencia
set_c =set_a.difference(set_b) #forma 1
print(set_c)
print(set_a - set_b)

#Diferencia simetrica (unión sin elementos en comun)
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)

#...LIST COMPREHENSION, listas con sintaxis abreviada
#este es el normal:
numbers = []
for element in range(1,11):
    numbers.append(element*2)
print(numbers)
#este es aplicando el concepto list comprehension

numbers_v2 = [element*2 for element in range (1,11)]
print(numbers_v2)

#agregando condiciones en List comprehension
#forma clasica
numbers.clear()
for i in range (1,11):
    if i % 2 == 0:
        numbers.append(i*2)
print(numbers)
# list comprehension
numbers_v2.clear()
numbers_v2 = [i*2 for i in range (1,11) if i % 2 == 0]
print(numbers_v2)

#Aplicando list compehesion a diccionarios
dict = {}
for i in range(1,5):
    dict[i] = i*2
print(dict)

dict_2 = {i: i*2 for i in range (1,5)}
print(dict_2)

countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1,100)
print (population)

population_v2 = {country: random.randint(1,100) for country in countries}
print(population_v2)

#unir listas
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

print(list(zip(names,ages))) #esto resulta en tuplas

new_dict = {name: age for (name, age) in zip (names, ages)} #no tuplas, por un for comprehension

#conditions dictionary compehension

result = {country:population for (country, population) in population_v2.items() if population >20 }
print(result)

text = 'Hola, soy Sebastian'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)

#funciones

def my_print(text):
    print(text*2)

my_print('Hola ')

#funciones return
sum = 0
for x in range (1,10):
    sum+=x
print (sum)

def sum_with_range(a,b):
    sum = 0 # variables internas de la función.
    for x in range (a,b):
        sum += x
    print(sum)
    return sum

result = sum_with_range(2,50)
print(result)
print(sum_with_range(2,50))

#multiples return

def find_volume(length=1,width=1,depth=1): #valores por defecto
    return length * width * depth, width, "hola"

result = find_volume(width=2)

print(result)

# the scope of variables in python, es la aplicación de la variable (alcance)

price = 100
print(price) # alcance en todo el archivo
def increment():
    print(price) #ejemplo, se puede utilizar en una función. pero si la declaramos dentro, no es globarl
    
# funciones lambdas

def increment(x):
    return x + 1
increment2 = lambda x : x + 1 #función lambda
result = increment(10)
print(result)
print(increment2(10))

full_name = lambda name, last_name: f'Full name es {name.title()} {last_name.title()}'

text = full_name('nicolas', 'perez casas')
print(text)

#Higher order function: una función dentro de otra función

def increment3(x):
    return x + 1

def high_ord_func(x,func):
    return x + func(x)

result = high_ord_func(2, increment)
print (result)
 
high_ord_func2 = lambda x, func: x + func(x) #utilizando lambda
result = high_ord_func2(2, increment3)
print(result)

#map es transformaciones a una lista dada de elementos.

numbers = [1,2,3,4]
numbers_v2 = []

for i in numbers:
    numbers_v2.append(i*2)
print(numbers)
print(numbers_v2)

numbers_v3 = list(map(lambda i: i*2, numbers)) #la función map asigna a lambda cada iterable de la lista numbers

print(numbers_v3)

numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7]

result = list(map(lambda x, y: x + y, numbers_1, numbers_2)) # solo resulta una lista de 3 valores. 
print(result)

items = [
    {
        'product': "camisa",
        'price': 100
    },
    {
        'product': "pantalones",
        'price': 200
    },
    {
        'product': "zapatos",
        'price': 300
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)
print(items[0]['price'])

def add_taxes(item):
    item['taxes'] = item['price']*.19
    return item

new_items = list(map(add_taxes, items)) # esto hace que se modifique el array original y puede ser un comportamiento no deseado
print(new_items)

#Para que no se modifique el array original, durante la función se recomienda hacer una copia. Esto se llama mutabilidad

def add_taxes2(item):
    new_item = item.copy() # copia el diccionario pero no se trae esa referencia.
    new_item['taxes'] = new_item['price']*.19
    return new_item

#Función Filter

numbers = [1,2,3,4,5,]
new_numbers = list(filter(lambda x: x % 2 ==0, numbers)) # colocar en lista los numeros que se dividan entre 2 y de 0 de residuo
print(new_numbers)

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print('Primero ->', matches)
print(len(matches))

new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))
print(new_list)


#función reduce, reduce a un solo valor

import functools

numbers = [1,2,3,4]

result = functools.reduce(lambda counter, item: counter + item, numbers) #reduce solo utiliza dos parametros y puede iterar solo de a dos elementos por iteración
print(result)

#Módulos

#Permite empezar a modular la aplicación, son los imports

import sys #da información del sistema operativo
print(sys.path)

import re #expresiones regulares
text = 'Mi número de telefono es 3113336865, el código es 57 y mi número de la suerte es 3'
result = re.findall('[0-9]+', text)
print(result)

import time #Para horas y fechas
timestamp = time.time() #formato maquina
print(timestamp) 
local= time.localtime()
print(local) #formato estructura time
fecha = time.asctime(local) #formato fecha ddd mmm dd hhhh
print(fecha)

import collections #utilidad para manejar listas
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)

#Creación de modulos propios
#Cualquier archivo se puede comportar como módulo. 
#se creara un modulo en mod.py

import utils

keys, values = utils.get_population()
print(keys, values)

data = [
    {
        'Country': 'Colombia',
        'Population': 500
    },
    {
        'Country': 'Bolivia',
        'Population':300
    }
]
result = utils.population_by_country(data,'Colombia')
print(result)

#MODULOS COMO SCRIPTS __name__ y __main__  dualidad

#Si hacemos import a un archivo .py que se pueda ejecutar, se ejecutará junto con el actual desde donde estemos llamando. 
#Esto se soluciona primero, para los archivos que se vayan a usar como modulo/script dejar su ejecución dentro de una función
#Luego, puede que yo quiera import desde un archivo controlando lo que quiero ejecutar pero a la vez si lo ejecuto individual, se ejecute sin indicar nada. 
#Para esto usamos if __name__ = '__main__': xxx para indicar que ejecutar cuando se llame desde la terminal.

#PAQUETES packages
'''
from pkg.mod1 import func_1, func_2
from pkg.mod2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())
#en la versión 3 de python con lo anterior era suficiente para usar un paquete
#sin embargo, las versiones anteriores utilizaban un archivo llamado __init__.py:
'''
import pkg
print(pkg.URL)
print(pkg.mod1.func_1()) # esto solo funciona si en __init__.py hace import a todos los modulos que se requieran

#iterables

for i in range(1,10):
    print(i)

my_iter = iter(range (1,11))
print(my_iter) #sale literalmente ragne (1,11) si no dejamos "iter"

print(next(my_iter)) # hace que el iterable se realice "manualmente". Por cada next se hace una iteración
print(next(my_iter))
print(next(my_iter))

#Errores en Python
#print(0/0)
#print(hola)

suma = lambda x,y: x + y
assert suma(2,2) == 4 # puede verificar si la función es correcta y en caso contrario sale un error
#esto se llama pruebas unitarias y hay varios metodos para hacerlas.

age = 18

if age < 18:
    raise Exception('No se permite menores de edad') #lanzar un error por criterio del programa que al producirse detiene la ejecución

#Manejo de errores
try:
    print(0/0)
except ZeroDivisionError as error: #esto se uede hacer en cualquier parte dentro del bloque del ty
    print(error)

print('hola')

#Leer un archivo de texto

file = open('./file.txt')
print(file.read())
file.close() #cierra y libera espacio en memoria

file = open('./file.txt')
print(file.readline()) #linea a linea
print(file.readline())
print(file.readline())

file.close() #cierra y libera espacio en memoria

file = open('./file.txt')

for line in file:
    print(line)
file.close()

with open('./file.txt') as file: #forma para que python cierre el archivo y es la mas comun utilizada
    for line in file: 
        print(line)

#editar archivos o escribir en uno
with open('./file.txt','r+') as file: #el segundo argumento es el que da permisos, en este caso lectura y escritura
    for line in file: 
        print(line)
    file.write('\n Nuevo texto en el archivo')

#LEER CSV (VER ARCHIVO read_csv.py)
import read_csv
