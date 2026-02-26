### Condicionales ###

# my_conditionals = True
my_conditionals = False # esto no imprime la condicion

if my_conditionals:# Es lo mismo que if my_conditionals == True
    print("se ejecuta la condicion del if")

my_conditionals = 5 * 5 # 10 = Opcion1: / 15 = Opcion2 

if my_conditionals == 10: # no se cumple
    print("se ejecuta la condicion del segundo if") # solo se imprime si es ==

if my_conditionals > 10 and my_conditionals < 20: # la condicion no se cumple
    print("Opcion1 Es mayor que 10 y menor que 20")
elif my_conditionals == 25:
    print("Opcion2 Es igual que elif")
else:
    print("Opcion3 Es mayor o igual 10 o mayor igual 20 o distinto")

print("La ejecucion continua") # esta fuera de las condiciones y siempre se imprime

""" Otra clase """

my_string = "No estoy vacia" # si no le agregas informacion no imprime nada

if not my_string:
    print("Mi cadena de texto esta vacia")
if my_string: 
    print("Mi cadena de texto no es vacia") # imprime si tiene informacion
if my_string == "Mi cadena de textoooo":
    print("Estas cadenas de texto coinciden") #imprime si es igual

# OTROS TIPS

# si mi condicion es menor que 10 igual que 20 o mayor que 50

my_conditionals = 15

# Opcion A: La más común y clara
if (my_conditionals > 10 and my_conditionals < 20) or my_conditionals > 50:
    print("Cumple la condicion A")
# Oción B: Estilo Python (más corto)
if 10 < my_conditionals < 20 or my_conditionals > 50:
    print("Cumple la condicion B")


