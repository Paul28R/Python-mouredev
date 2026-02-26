### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

""" CAMBIAR TUPLAS POR LISTA 1 """


my_list = list(my_tuple) #cambia tupla por lista

my_list[1] = 1.00 #modifica la lista

my_tuple = tuple(my_list) #cambia lista por tupla

print(my_tuple) 

""" CAMBIAR TUPLAS POR LISTA 2 """

tupla = (1, 2, 3)

lista = [*tupla] # Desempaqueta los elementos dentro de una nueva lista

lista[0] = 100

tupla = [*lista]

""" CAMBIAR TUPLAS POR LISTA 3 """



print(tupla)
