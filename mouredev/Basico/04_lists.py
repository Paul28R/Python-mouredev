### Lists ###

my_list = [35, 24, 62, 52, 30, 30, 17]

# print(my_list)
# print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]

# print(type(my_list))
# print(type(my_other_list))

# print(my_other_list[0])
# print(my_other_list[-1])
# print(my_other_list[1])
# print(my_other_list[-2])
# print(my_other_list[-4])
# print(my_other_list[3])
# print(my_list.count(30))

my_other_list.append("Mouredev")
print(my_other_list)

my_other_list.insert(1, "brown")
print(my_other_list)

# my_other_list.remove("brown")
# print(my_other_list)

# my_list.remove(30)
# print(my_list)

# print(my_list.pop())
# print(my_list)

# print(my_list.pop(2))
# print(my_list)

# my_pop_element = my_list.pop(2)
# print(my_pop_element)

my_other_list.insert(1, "rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_new_list = my_list.copy()
print(my_new_list)


del my_list[2]
print(my_list)

# my_list.clear()
# print(my_list)

my_list.append(35)
print(my_list)


my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola python"
print(my_list)
print(type(my_list))
