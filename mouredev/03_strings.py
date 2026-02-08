### strings ###

# my_string = 'My String'
# my_other_string = 'mi otro string'

# print(my_string + " " + my_other_string)


# my_new_line_string = "este es un string \ncon salto de linea"
# print(my_new_line_string)

# my_tab_string = "\teste es un string con tabulacion"
# print(my_tab_string)

# my_space_string =  "\teste es un string con \nnescapado"
# print(my_space_string)

#Formato

name, surname, age = "Brais", "Moure", 35

print("Mi name is {} {} y mi edad es {}".format(name, surname, age))
print("Mi name is %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi name is {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(f)


language_slice = language[0:6:2]
print(language_slice)

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize()) #Primera letra mayuscula
print(language.upper()) #Todo mayuscula
print(language.count("t")) #Cuenta cuantas veces aparece el caracter
print(language.isnumeric()) #Comprueba si es numero
print("1".isnumeric()) #Comprueba si es un numero
print(language.lower()) #Todo minuscula
print(language.upper().isupper()) #isupper es para comprobar si esta mayuscula
print(language.startswith("py")) 
 