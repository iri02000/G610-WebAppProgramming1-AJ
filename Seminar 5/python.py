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

print("Python if else")

n = input()
n = int(n)

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 < n < 5:
    print("Not weird")
elif n % 2 == 0 and 6 < n < 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not weird")
