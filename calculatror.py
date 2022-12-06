print("*******************************************")
print("Simple calculator using python")
print("*******************************************")
num1 = int(input("Enter 1st int number = "))
print("*******************************************")
num2 = int(input("Enter 2nd int number = "))
print("*******************************************")

print("*******************************************")
print("Addition Press 1")
print("*******************************************")
print("Subtratioin Press 2")
print("*******************************************")
print("Multiplication Press 3")
print("*******************************************")
print("Division Press 4")
print("*******************************************")
print("Modulous Press 5")
print("*******************************************")
print("Expontial Press 6")
print("*******************************************")

input_conditon = int(input("Enter conditon = "))

if input_conditon == 1:
    print("*******************************************")
    print("Addition", num1, "+", num2, "=", num2+num2)
    print("*******************************************")

if input_conditon == 2:
    print("*******************************************")
    print("Subtration", num1, "-", num2, "=", num2-num2)
    print("*******************************************")

if input_conditon == 3:
    print("*******************************************")
    print("Multiplication", num1, "*", num2, "=", num2*num2)
    print("*******************************************")

if input_conditon == 4:
    print("*******************************************")
    print("Division", num1, "/", num2, "=", num2/num2)
    print("*******************************************")

if input_conditon == 5:
    print("*******************************************")
    print("Modulous", num1, "%", num2, "=", num2 % num2)
    print("*******************************************")

if input_conditon == 6:
    print("*******************************************")
    print("Expontial", num1, "**", num2, "=", num2**num2)
    print("*******************************************")

if input_conditon > 6:
    print("*******************************************")
    print("Enter valid input")
    print("*******************************************")
