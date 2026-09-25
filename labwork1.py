#Ex1
n=float(input("Enter circle radius: "))

area = 0
area = n*n*3.14

print("Circle area: ",area)

#Ex2
n=float(input("Enter the temperature in Celsius: "))

fahren=0
fahren=(n*9/5)+32

print(f"{n}(C) = {fahren}(F)")
#Ex3
n=int(input("Enter a number: "))

if n>1 and all(n % i != 0 for i in range(2, n)):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")

#Ex4
n = int(input("Enter a number: "))
if n>0 and n % 2 == 0 :
    

else :
    print(f"{n} is not a perfect number")

#Ex5
mycolorlist = ["red","white","blue","black","yellow"]


fav1 = input("What is your favourite color: ")
if fav1 in mycolorlist:
    print("Your color is in my list")
else:
    print("Your color is not in my list")

#Ex6
print(list(range(0,8)))
print(list(range(1,11,3)))
print(list(range(5,0,-1)))
print(list(range(6,-3,-2)))
#Ex7
def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")
#Ex8
def extract_even(l):
    even_list = []

    
    for item in l:
        if item % 2 == 0:
            even_list.append(item)

    return even_list



#Ex9
def remove_dollar_sign(s):

    return s.replace("$", "")

result = remove_dollar_sign(text)
print(f"Original: {text}")
print(f"Result: {result}")
#Ex10
def print_divisors(n):
    print(f"Divisors of {n}:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

number = int(input("Enter a number: "))
print_divisors(number)
#Ex11
print("A(x1,y1) and B(x2,y2)")
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

squrx = (x2-x1)**2
squry = (y2-y1)**2

distance = (squrx + squry)**0.5

print("Distance : ",distance)
#Ex12
def print_box_pattern(m, n):
    for i in range(m):
        for j in range(n):
        
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print() 

m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))
print_box_pattern(m, n)