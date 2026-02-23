### Classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

### def and self ###

class Person:
    def __init__(self, name, surname):
        self.name = name        # (pass) funciona si no hay nada
        self.surname = surname

my_person = Person("Brais", "Moure")
print(my_person.name + " " + my_person.surname)
print(f"{my_person.name} {my_person.surname}")

### self sin parametros ###

class Personn:
    def __init__(self):
        self.name = "Brais"
        self.surname = "Maure"

my_person1 = Personn()

###

class Persone:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"{self.full_name} está caminando")

my_person2 = Persone("Brais", "Moure")
print(my_person2.full_name)
my_person2.walk()

###

class Persone:
    def __init__(self, name, surname, alias ="Sin salida"):
        self.full_name = f"{name} {surname} ({alias})"

    def walk(self):
        print(f"{self.full_name} está caminando")

my_person2 = Persone("Brais", "Moure")
print(my_person2.full_name)
my_person2.walk()

my_other_person = Persone("Brais", "Moure", "Mouredev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)


my_other_person.full_name = 666
print(my_other_person.full_name)