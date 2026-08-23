
'''


#Question 1:

for i in range (1,11):
    print(i,end=' ')


#Question 2:

for i in range (10,0,-1):
    print(i,end=' ')


#Question 3:

for i in range (1,51):
    if i%2==0:
        print(i)


#Question 4:

for i in range (1,51):
    if i%2!=0:
        print(i)


#Question 5:

n=int(input("Enter the number :"))
for i in range (1,11):
    print(n,'x',i,'=',i*n)


#Question 6:

s=0
for i in range (1,101):
    s+=i
print(s)


#Question 7:

for i in range (1,11):
    print(i**2)


#Question 8:

for i in 'PYTHON':
    print(i)


#Question 9:

text = input("Enter a string: ")
count = 0
for i in text:
    if i in "aeiouAEIOU":
        count += 1
print("Vowels:", count)


#Question 10:

s=0
for i in range (1,101):
    if i%2==0:
        s+=i
print(s)


#Question 11:

n=int(input("Enter the number :"))
f=1
for i in range(1,n+1):
    f*=i
print(f)


#Question 12:

n=int(input("Enter the number: "))
c=0
for i in range(2,n):
    if n%i==0:
        c+= 1
if c==0:
    print("Prime")
else:
    print("Not Prime")


#Question 13:

for i in range(2,101):
    c=0
    for j in range(2,i):
        if i%j==0:
            c+=1
    if c==0:
        print(i)


#Question 14:

n=[10,45,23,89,12,67]
l=n[0]
for i in n:
    if i>l:
        l=i
print("Largest:",l)



#Question 15:

l=[10,-45,-23,89,-12,67]
p=0
n=0
for i in l:
    if i>0:
        p+=1
    else:
        n+=1
print("Positive:",p)
print("Negative:",n)


#Question 16:

t=str(input("Enter a string: "))
r=""
for i in t:
    r=i+r
print("Reverse:",r)


#Question 17:

s=(input("Enter the string :"))
ch=(input("Enter the character :"))
c=0
for i in s:
    if i==ch:
        c+=1
print("Count :",c)


#Question 23:

numbers = [10, 45, 23, 89, 12, 67]
largest = numbers[0]
second = numbers[0]
for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print("Second Largest:", second)

#Question 24:

num = int(input("Enter a number: "))
temp = num
sum = 0
for i in str(num):
    sum = sum + int(i) ** 3
if sum == temp:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


#Question 24:
n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


#Question 25:

text = input("Enter a string: ")
reverse = ""
for i in text:
    reverse = i + reverse
if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


#Question 26:

numbers = [10, 20, 10, 30, 20, 40]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i])


'''























