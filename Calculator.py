from math import *


def diff(n, mid):
    if (n > (mid * mid * mid)):
        return (n - (mid * mid * mid))
    else:
        return ((mid * mid * mid) - n)


def cubicRoot(n):
    start = 0
    end = n
    e = 0.0000001
    while (True):

        mid = (start + end) / 2
        error = diff(n, mid)

        if (error <= e):
            return mid

        if ((mid * mid * mid) > n):
            end = mid

        else:
            start = mid


print("Welcome to My Calculator !")
print("Enter the required code for your operation as under \n"
      "1 - Addition\n"
      "2 - Multiplication\n"
      "3 - Subtraction\n"
      "4 - Division\n"
      "5 - Exponents/Powers\n"
      "6 - Roots(Square/Cube)\n"
      "7 - Logarithmic function\n"
      "8 - Trigonomtric calculation(sin/cos/tan)\n ")
flag = True
while(flag):
    code = int(input("Enter the required code = "))
    if(code<6):
        num1 = float(input("Enter the first number = "))
        num2 = float(input("Enter the second number = "))
        if(code==1):
            print(num1+num2)
        elif(code==2):
            print(num1-num2)
        elif(code==3):
            print(num1*num2)
        elif(code==4):
            print(num1/num2)
        else:
            print(pow(num1 , num2))
    else:
        if(code==6):
            root = float(input("Enter 1 for square root and 2 for cube root = "))
            num = float(input("Enter the operand = "))
            if(root==1):
                print(sqrt(num))
            elif(root==2):
                print(cubicRoot(num))
            else:
                print("Please enter a valid option(1/2)")
        elif(code==7):
            num = float(input("Enter the operand = "))
            base = float(input("Enter the base for the log function = "))
            print(log(num , base))
        elif(code==8):
            type = float(input("Enter 1 for sin, 2 for cos and 3 for tan = "))
            num = float(input("Enter the angle in radian = "))
            if(type==1):
                print(sin(num))
            elif(type==2):
                print(cos(num))
            elif(type==3):
                print(tan(num))
            else:
                print("Please enter valid input[1-3]")
        else:
            print("Please enter valid input[1-8]")
    fcheck = float(input("Do you want to perform another calculation? Enter 1 if so else enter 0 to exit "))
    if(fcheck==0):
        flag = False
        print("Thank You!")



