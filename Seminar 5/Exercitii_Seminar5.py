# print ("Aritmetic Operations")
# a=1
# b=1
# print (a, b)

# print(3+2)
# print(3-2)
# print(3*2)

# print("Finding the percentage") #incomplet pentru ca nu l-am facut in dictionary data type

# print("CAti elevi sunt?")
# n=input()
# i=0
# while i<3:
#     input(b)
# print("Krishna 67 68 69")
# print("Arjun 70 98 63")
# print("MAlika 52 56 60")
# print("Malika")
# print()

# print(
#     "Media cui vreti sa o calculati? Putem calcula deocamdata numai media lui Krishan. Scrie Krishan!"
# )
# name = input()
# if name == "Krishan":

#     a = (67 + 68 + 69) / 3
#     format_a = "{:.2f}".format(a)
#     print(format_a)
# else:

#     print(" Vrem sa calculam numai media lui Krishan")

# print("Python if else")

# n = input()
# n = int(n)

# if n % 2 == 1:
#     print("Weird")
# elif n % 2 == 0 and 2 < n < 5:
#     print("Not weird")
# elif n % 2 == 0 and 6 < n < 20:
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Not weird")

# print("Introduction to Sets")

# emptyset = set()

# x = int(input("Cate inaltimi vreti sa introduceti? "))
# i = 0
# while i < x:
#     try:
#         emptyset.add(int(input("Introduceti inaltimea platelor: ")))
#     except:
#         print("Invalid input")
#     i = i + 1

# average = sum(emptyset) / len(emptyset)
# format_a = "{:.2f}".format(average)
# print("Media inaltimii plantelor este de: ", format_a)
# print("Toate inaltimile in ordinea crescatoare: ", emptyset)

# print("Python: Division")
# a = int(input("Introduceti numarul a: "))
# b = int(input("Introduceti numarul b: "))

# print("The integer division of a and b is: ", int(a / b))
# print("The float division of a and b is: ", float(a / b))

# print("Lists")
# print(
#     "These are the commands: \n1. insert i e : Insert integer at position .\n2. print: Print the list.\n3. remove e : Delete the first occurrence of integer .\n4. append e : Insert integer at the end of the list.\n5. sort: Sort the list.\n6. pop : Pop the last element from the list.\n7. reverse : Reverse the list.\n8. Exit"
# )

# # 1. insert i e : Insert integer at position .
# # 2. print: Print the list.
# # 3. remove e : Delete the first occurrence of integer .
# # 4. append e : Insert integer at the end of the list.
# # 5. sort: Sort the list.
# # 6. pop : Pop the last element from the list.
# # 7. reverse : Reverse the list.
# # 8. Exit

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# choise = 0
# while choise != 8:
#     choise = int(input(" Choose the command: "))
#     if choise == 1:
#         a = int(
#             input("At what position do you want to add a value in the list?"))
#         a_insert = int(input("Input the value that you want to insert: "))
#         list.insert(a - 1, a_insert)
#         print(list)

#     elif choise == 2:
#         print(list)

#     elif choise == 3:
#         a_remove = int(input("What value do you want to remove?"))
#         list.remove(a_remove)
#         print(list)

#     elif choise == 4:
#         a_append = int(
#             input("What value do you want to add at the end of the list? "))
#         list.append(a_append)
#         print(list)

#     elif choise == 5:
#         list.sort()
#         print(list)

#     elif choise == 6:
#         print("You are going to delete the last element of the list! ")
#         delete = input(
#             "Do you want to delete the last element. Please write yes or no: ")
#         if delete == "yes":
#             list.pop()
#         print(list)
#     elif choise == 7:
#         list.reverse()
#         print(list)

# print("Tuples")

# n = int(input("How many elem does the tuple have? "))
# t = ()
# i = 0
# t_el = input("Input the elements : ").split()

# def string_toint(t_el):
#     for i in t_el:
#         t_el.append(int(t_el[0]))
#         t_el.remove(t_el[0])
#     return t_el

# t_el = string_toint(t_el)

# print(t_el)

# t = (tuple(t_el))
# print(t)
# print(hash(t))
