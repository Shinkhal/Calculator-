print("***WWLCOME TO PYTHON CALCULATOR***")

#1. ADD
#2. SUBTRACT
#3. MULTIPLY
#4. DIVIDE
#5. SWUARE
#6. CUBE


print("Select the operation")
print("1. ADD")
print("2. SUBSTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. SQUARE")
print("6. CUBE")

operation = input()
if operation == "1":
    num1 = input("Enter first number ")
    num2 = input("Enter second number ")
    print("The result is : " + str(int(num1) + int(num2)))
elif operation == "2" :
    num1 = input("Enter first number ")
    num2 = input("Enter second number ")
    print("The result is : " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter first number ")
    num2 = input("Enter second number ")
    print("The result is : " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter first number ")
    num2 = input("Enter second number ")
    print("The result is : " + str(int(num1) / int(num2)))
elif operation == "5":
    num1 = input("Enter Number")
    print("The result is : " +str(int(num1) * int(num1)))
elif operation == "6":
    num1 = input("Enter the number")
    print("The result is : " + str(int(num1) ** int(num1)))
else:
    print("Invalid Entry")

