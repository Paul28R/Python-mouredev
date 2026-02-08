### Sets ###

my_set = set() # No es una estructura ordenada
my_other_set = {} # Esto es un Dict

print(type(my_set))
print(type(my_other_set)) # Dict

my_other_set = {"paul", "rodriguez", 30} # sin llave y dato pasa a ser un set

print(type(my_other_set)) # ahora imprime set

my_other_set.add("paul28") # Agrego informacion

my_other_set.add("paul28") # No duplica informacion.

print(my_other_set)
print(len(my_other_set)) # len() Cuenta cada elemento

print("paul" in my_other_set)
print("mouri" in my_other_set)

my_other_set.remove("paul") #elimina elemento en lista
print(my_other_set)

print(len(my_other_set))

my_set = {"paul", "rodriguez", 30} 

my_list = list(my_set)

print(my_list)
print(my_list[0])
print(my_list[1])

my_other_set = {"kotlin", "swift", "python", 30}

my_new_set = my_set.union(my_other_set) # Union de 2 set
# Alimprimir no acepta duplicados
# pero le agregamos mas datos sin variables con ({})
print(my_new_set.union(my_new_set).union(my_set).union({"javascripts", "C#"})) 

print(my_new_set.difference(my_set)) # diferencias entre sets

