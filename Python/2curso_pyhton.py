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


