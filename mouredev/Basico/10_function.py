### Functions ###

def my_function():
    print('este es una funcion')

my_function()#Llamada de la function


### Functions ###
def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)# suma 12
sum_two_values(54754, 71231) # suma 125985
sum_two_values('5', '7') # concadena 57
sum_two_values(1.4, 4.2) # float

### Functions ###
def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

#diferencia entre return y print: 
# print() solo muestra en la pantalla(termila). no 'guarda' el resultado.
# return Es como si la funcion te entregara un paquete. Ese valor 'sustituye'
# a la llamada de la funcion y permite guardarlo en una variable para usarlo despues

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "Moure",name = "Brais")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "Mouredev")

def print_texts_upper(*texts): #para pasarle muchos parametros
    for text in texts:
        print(text.upper())

print_texts_upper("Hola", "python", "Mouredev")
print_texts_upper("Hola")