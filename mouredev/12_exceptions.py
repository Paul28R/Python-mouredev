### Exception Handling ###

numberone = 5 
numbertwo = 1
numbertwo = "1"



try:
    print(numberone + numbertwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce
    print("Se ha producido un error")


# try except else 

try:
    print(numberone + numbertwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # se ejecuta si no se produce
    print("La ejecucion continuea correctamente")
finally: # Opcional
    # Se ejecuta
    print("La ejecucion continua")

# Exceptions por tipo

try:
    print(numberone + numbertwo)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")

# captura de la informacion de la exception

try:
    print(numberone + numbertwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as Exception:
    print(Exception)