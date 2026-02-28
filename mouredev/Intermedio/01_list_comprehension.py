### List Comprehension ###


# Crear una lista con los n primeros numeros cuadrados
cuadrados = []
for i in range(5):
    cuadrados.append(i**2)
print(f"Resultado: {cuadrados}")
print("----------------------")
# Lista apartir de un iterable(lista,rango,cadena)
cuadrados_lc = [i**2 for i in range(5)]
print(f"Resultado: {cuadrados_lc}")
# Resultado: [0, 1, 4, 9, 16]

# Filtrado con condicionales (if)
# Fórmula: [expresión for elemento in iterable if condición]
cuadrados_pares = [i**2 for i in range(10) if (i**2) % 2 == 0]
print(f"Resultado: {cuadrados_pares}")

# Condicional y mayor que:
cuadrados_pares_lc = [i**2 for i in range(10) if (i**2) % 2==0 if (i**2) > 20]
print(f"Resultado: {cuadrados_pares_lc}")

###############################################################################

lista = [1,2,3,4,5]
# Ciclo for normal
cuadrados = []
for x in lista:
    cuadrados.append(x**2)
print(f"Resultado: {cuadrados}")
# Lista comprehencion:
cuadrados = [x**2 for x in lista if x % 2 == 0]
print(cuadrados)

#Ciclo normal Matrix
matrix = []
for _ in range(3):
    lista_interna = []
    for i in range(1,4):
        lista_interna.append(i)
    matrix.append(lista_interna)
print(matrix)

#
matrix = [[i for i in range(1,4)]for _ in range(3)]
print(matrix) 







