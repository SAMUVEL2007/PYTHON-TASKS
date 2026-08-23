


#1.Write a program to check whether a number is even or odd.

num=float(input("Enter the number :"))
if num%2==0:
    print("Number is even...")
else:
    print("Number is odd...")


#2.Write a program to check whether a person is eligible to vote (age ≥ 18).

age=int(input("Enter the age :"))
if age>=18:
    print("A person is eligible to vote...")
else:
     print("A person is not eligible to vote...")


#3.Write a program to check whether a student passes or fails (marks ≥ 40).

mark=float(input("Enter the mark :"))
if mark>=40:
    print("A student is pass...")
else:
    print("A student is fail...")


#4.Write a program to check whether a number is positive or negative.
num=float(input("Enter the number :"))
if num>=0:
    print("Number is positive...")
    if num==0:
        print("But the number is zero...")
else:
    print("Number is negative...")


#5.Write a program to assign grades based on marks:
#90+ → A
#75–89 → B
#50–74 → C
#Below 50 → Fail
mark=float(input("Enter the mark :"))
if mark>=90:
    print("Grade is A...")
elif mark>=75:
    print("Grade is B...")
elif mark>=50:
    print("Grade is C...")
else:
    print("A student is fail...")


#6.Write a program to find the largest among three numbers.
num1=float(input("Enter the number 1 :"))
num2=float(input("Enter the number 2 :"))
num3=float(input("Enter the number 3 :"))
if num1>num2 and num1>num3:
    print("Number 1 is largest...")
elif num2>num1 and num2>num3:
    print("Number 2 is largest...")
elif num3>num1 and num3>num2:
    print("Number 3 is largest...")
else:
    print("All the 3 numbers are equal...")


#7.Write a program that takes a number (1–7) and prints the corresponding day of the week.
num=int(input("Enter the number 1 to 7 :"))
if num==1:
    print("Day 1 is Monday...")
elif num==2:
    print("Day 2 is Tuesday...")
elif num==3:
    print("Day 2 is Wednesday...")
elif num==4:
    print("Day 4 is Thursday...")
elif num==5:
    print("Day 5 is Friday...")
elif num==6:
    print("Day 6 is Saturday...")
elif num==7:
    print("Day 7 is Sunday...")
else:
    print("The number is not in 1 to 7...")


#8.Write a program to perform a simple calculator operation (+, -, *, /) based on user choice.
num1=float(input("Enter the number 1 :"))
num2=float(input("Enter the number 2 :"))
op=str(input("Enter the operation (add,sub,mul,div) :"))
if op=='add':
    print("num1 + num2 = ",num1+num2)
elif op=='sub':
    print("num1 - num2 = ",num1-num2)
elif op=='mul':
    print("num1 * num2 = ",num1*num2)
elif op=='div':
    print("num1 / num2 = ",num1/num2)
else:
    print("Enter the operation those (add,sub,mul,div) only ...")


#9.Write a program to validate login:
#If username is correct
#Then check password
#If correct → Login success
#Else → Wrong password
#Else → Invalid username
name=str(input("Enter the username :"))
password=str(input("Enter the password :"))
if name=='SAM':
    print("Valid usernamet...")
    if password=='12@45':
        print("Correct password...")
        print("Login is success...")
    else:
        print("Wrong password...")
else:
    print("Invalid username...")


#10.Traffic Signal System
#Write a program to print action based on signal:
#Red → Stop
#Yellow → Get Ready
#Green → Go
#👉If invalid signal → print error
color=str(input("Enter traffic signal color: "))
if color=="red":
    print("Stop...")
else:
    if color=="yellow":
        print("Get Ready...")
    else:
        if color=="green":
            print("Go...")
        else:
            print("Error:Invalid signal...")














