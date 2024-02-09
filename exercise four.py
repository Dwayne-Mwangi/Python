# while True:
#
#     try:
#
#         maths = int(input("Maths: "))
#
#         break
#
#     except ValueError:
#
#         print("Invalid input. Please enter a number.")

       #/-----Variables------/#

maths = int(input("Maths: "))
if maths > 100 or maths < 0:
    print("Invalid Input")


english =  int(input("English: "))
if english > 100 or english < 0:
    print("Invalid Input")


kiswahili =  int(input("Kiswahili: "))
if kiswahili > 100 or kiswahili < 0:
    print("Invalid Input")


chemistry =  int(input("Chemistry: "))
if chemistry > 100 or chemistry < 0:
    print("Invalid Input")


physics =  int(input("Physics: "))
if physics > 100 or physics < 0:
    print("Invalid Input")


biology =  int(input("Biology: "))
if biology > 100 or biology < 0:
    print("Invalid Input")


#-----Computation----#

total =  (maths + english + kiswahili + chemistry + physics + biology)

average = (total / 6)

print(f"Average: {average}")


#----If Statement Grading----#

if average >= 71:
    print("A+")

elif average >= 61:
    print("B")

elif average >= 51:
    print("C")

elif average >= 40:
    print("D")

else:
    print("E")


