### Loops ###

# While 1

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")


# While 2

while my_condition < 20:
    my_condition += 1 # two it doesn't stop because it doesn't reach 15
    if my_condition == 15: # a conditional inside a loop
        print("Mi condicion es 15 se detiene")
        break # stop the loop
    print(my_condition)

print("La ejecucion continua")

###### For ######

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure")
for element in my_tuple:
    print(element)

my_set = {"paul", "rodriguez", 30}
for element in my_set:
    print(element)

my_dict = {"nombre":"brais", "apellido":"moure", "edad":35, 1:"python"}
for element in my_dict.values(): # sin values solo imprimira las llaves y no los valores 
    print(element)
    if element == 35:
        print("bucle cerrado")
        break # (continue) hara que el bucle continue  
    print("Se ejecuta")

my_dict = {"nombre":"brais", "apellido":"moure", "edad":35, 1:"python"}
for element in my_dict.values(): # sin values solo imprimira las llaves y no los valores 
    print(element)
    if element == 35:
        print("bucle cerrado")
        break # (continue) hara que el bucle continue  
    print("Se ejecuta")
    
         
