print ("~~Mini Calculator~~")
num1 = float(input("enter first number here: "))
num2 = float(input("enter second number here: "))
print ("press 1 for subtraction \n press 2 for addition\npress 3 for division \npress 4 for multiplication")
choice = int(input("enter your choice from 1-4: "))
if choice == 1:
    print ("The subtraction of given two numbers is",num1 - num2)
elif choice == 2:
    print ("The addition of given two numbers is",num1 + num2)
elif choice == 3:
    print ("The divition of given two numbers is",num1 / num2)
elif choice == 4:
    print ("The multiplication of given two numbers is",num1 * num2)
else:
    print ("The value is Invalid Input")