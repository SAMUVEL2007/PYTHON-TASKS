
'''

#QUESTION 1:

balance=5000
amount=int(input("Enter withdrawal amount: "))
if amount<=balance:
    print("Withdrawal successful")
else:
    print("Insufficient Balance")


#QUESTION 2:

username=input("Enter username: ")
password=input("Enter password: ")
if username=="admin":
    if password=="1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")


#QUESTION 3:

amount=float(input("Enter purchase amount: "))
if amount>5000:
    discount=amount*20/100
    final=amount-discount
    print("Discount =",discount)
    print("Final amount =",final)
else:
    print("No discount")
    print("Final amount =",amount)


#QUESTION 4:

mark=int(input("Enter mark: "))
if mark>=90:
    print("A")
elif mark>=75:
    print("B")
elif mark>=60:
    print("C")
else:
    print("Fail")



#QUESTION 5:

correct_password="admin123"
for attempt in range(3):
    password=input("Enter password: ")
    if password==correct_password:
        print("Login successful")
        break
    else:
        print("Wrong password")
else:
    print("Account locked")


#QUESTION 6:

balance = 5000
while True:
    print("1.Balance")
    print("2.Withdraw")
    print("3.Deposit")
    print("4.Exit")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Balance =",balance)
    elif choice==2:
        amount=int(input("Enter amount: "))
        if amount<=balance:
            balance=balance-amount
            print("Withdrawal successful")
        else:
            print("Insufficient Balance")
    elif choice==3:
        amount=int(input("Enter deposit amount: "))
        balance=balance+amount
        print("Deposit successful")
    elif choice==4:
        print("Thank you")
        break
    else:
        print("Invalid choice")


#QUESTION 7:

products=["Laptop", "Mobile", "Out of Stock", "Mouse"]
for product in products:
    if product=="Out of Stock":
        continue
    print(product)


#QUESTION 8:

vehicles=["TN01AB1234", "TN22CD5678", "TN30EF9999"]
search=input("Enter registration number: ")
for vehicle in vehicles:
    if vehicle==search:
        print("Vehicle found")
        break
else:
    print("Vehicle not found")


#QUESTION 9:

emails=["abc@gmail.com","hello@gmail.com","invalidemail","test@yahoo.com"]
for email in emails:
    if "@" not in email:
        continue
    print("Valid:", email)


#QUESTION 10:

number=int(input("Enter number to search: "))
for i in range(1, 101):
    if i==number:
        print("Number found")
        break
else:
    print("Number not found")


#QUESTION 11:

age=int(input("Enter your age: "))
salary=float(input("Enter your salary: "))
if age>=21:
    if salary>=30000:
        print("Loan approved")
    else:
        print("Salary is too low")
else:
    print("Age requirement not met")


#QUESTION 12:

mark=int(input("Enter mark: "))
documents=input("Do you have required documents? (yes/no): ")
if mark>=60:
    if documents=="yes":
        print("Admission approved")
    else:
        print("Submit documents")
else:
    print("Not eligible")


#QUESTION 13:

for i in range(1,11):
    status=input("Enter attendance (Present/Absent): ")
    if status=="Present":
        print("Employee",i," is present")


#QUESTION 14:

while True:
    login=input("Enter login status: ")
    if login=="suspicious":
        print("Alert!")
        break
    print("Monitoring...")


#QUESTION 15:

inputs = [10,20,-5,30,40]
for value in inputs:
    if value<0:
        continue
    print("Testing:",value)


#QUESTION 16:

def payment():
    pass
print("Payment function is ready for implementation")


#QUESTION 17:

customer_id=int(input("Enter customer ID: "))
for i in range(1, 1001):
    if i==customer_id:
        print("Customer found")
        break
else:
    print("Customer id is not in range ")


records=[101,102,-1,104,105]
for record in records:
    if record<0:
        continue
    print("Processing:",record)


#QUESTION 18:

for i in range(100):
    print("Processing student", i + 1)


password = ""
while password != "admin123":
    password = input("Enter password: ")
print("Login successful")


#QUESTION 19:

while True:
    item = input("Enter item: ")
    if item == "exit":
        print("Thank you")
        break
    if item == "unavailable":
        print("Item unavailable")
        continue
    print("Order placed:", item)


'''




