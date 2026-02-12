### Diccionarios ###

my_dict = dict() # Dict 
my_other_dict = {} # Dict

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"nombre":"brais", "apellido":"moure", "edad":35, 1:"python"}

my_dict = {
    "nombre":"brais", 
    "apellido":"moure", 
    "edad":35, 
    "lenguajes":{"python", "swift", "kotlin"},
    1:1.7
    }
print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

my_dict["nombre"] = "pedro" # cambio de valor
print(my_dict["nombre"]) # imprime el valor dentro de la clave


my_dict["calle"] = "calle MoureDev" # si la clave no aparece, se agrega automaticamente
print(my_dict) 

del my_dict["calle"]
print(my_dict)

print("moure" in my_dict)
print("mouri" in my_dict)
print("apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys(("nombre", 1)))

print(list(my_dict))
print(tuple(my_dict))
print(set(my_dict))