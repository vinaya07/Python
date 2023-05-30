"""
Problem: Write a program that reads whole numbers typed by the user until a zero is entered, then prints the number of positive numbers that were entered. Sample run:
Enter a number: 3
Enter a number: -2
Enter a number: 5
Enter a number: 6
Enter a number: -100
Enter a number: 70
Enter a number: 22
Enter a number: 68
Enter a number: 0
6 positive numbers were entered.
"""

count = 0

while True:
    n = int(input("Enter a number (enter 0 to stop): "))
    if n > 0:
        count += 1
    if n == 0:
        break

print(count, "positive numbers were entered")

"""
Problem: In mathematics, the Fibonacci sequence is defined such that each Fibonacci number is the sum of the two preceding ones, starting from 0 and 1. That is, F1 = 0, F2 = 1, F3 = 1, F4 = 2, ..., Fn = F(n-1) + F(n-2). Write a program that given an input n, outputs the first n Fibonacci numbers. The format of output is that at most 4 numbers can be displayed in a row. Sample run:
Enter a positive number: 6
0 1 1 2 
3 5
Enter a positive number: 10
0 1 1 2
3 5 8 13
21 34

"""


def printFibonacciNumbers(n):
    f1 = 0
    f2 = 1
    count = 0
    while count < n:
        if count % 4 == 0:
            print("")
        print(f1, end=" ")
        temp = f1 + f2
        f1 = f2
        f2 = temp
        count += 1


n = int(input("Enter a positive number: "))
printFibonacciNumbers(n)

"""
Problem: Given an input number n, print a diamond shape with 2*n-1 rows.
Sample run:
Enter a positive number: 3 
   x 
  xxx  
 xxxxx
  xxx
   x
"""
n = int(input("Enter a positive number:"))

for i in range(n):
    print(" " * (n - i), "*" * (i * 2 + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i), "*" * (i * 2 + 1))

"""
Problem: A palindrome is a number or a text phrase that reads the same backwards as well as forwards. Examples of palindromes are 123321, 1234321, 55555, 22, 454, 1, 0. Write a program that reads in a positive integer number, and prints out whether or not that number is a palindrome. Sample run:
Enter a positive number: 12321
12321 is a palindrome
Enter a positive number: 1234
1234 is not a palindrome
"""
num = int(input("Enter a positive number:"))
temp = num
rev = 0
while num > 0:
    a = num % 10
    rev = rev * 10 + a
    num = num // 10
if temp == rev:
    print(temp, "is a Palindrome")
else:
    print(temp, "is not a Palindrome")

"""
Problem: A car dealer earns a base wage of $36.25 per hour up to their normal work week of 37 hours. Only whole hours are counted. If he works more hours than that (overtime) he gets paid at 1.5 times his normal rate for the overtime. If he sells more than 5 cars in a week, he gets a bonus of $200 per car from the 6th car sold. Write a program that takes as input the number of hours worked and the total number of cars sold for the week, and outputs the car dealer’s total salary for the week.
Examples:
How many hours were worked? 41
Total number of cars sold for the week? 10
The salary is 2558.75
How many hours were worked? 36
Total number of cars sold for the week? 3
The salary is 1305.0

"""

hours_worked = int(input("How many hours were worked? "))
cars_sold = int(input("Total number of cars sold for the week? "))

if hours_worked <= 37:
    base_pay = hours_worked * 36.25
else:
    base_pay = 37 * 36.25 + (hours_worked - 37) * 36.25 * 1.5

if cars_sold > 5:
    bonus = (cars_sold - 5) * 200
else:
    bonus = 0

total_salary = base_pay + bonus
print("The salary is ", total_salary)

"""
Problem: The grades at a university are awarded based on the marks awarded for the course out of 100. Marks of 85 or above receive the grade of 7. Marks less than 85 but that are 75 or above receive the grade of 6. Marks less than 75 but that are 65 or above receive the grade of 5. Marks less than 65 but that are 50 or above receive the grade of 4. Anything less than 50 gets the grade of F. Write a program that asks the user to input the marks and prints the grade awarded.
Example:
How many marks? 85
Grade awarded: 7

"""
a = float(input('How many marks? '))

if a >= 85:
    print("Grade awarded: 7")
elif 75 <= a < 85:
    print("Grade awarded: 6")
elif 65 <= a < 75:
    print("Grade awarded: 5")
elif 50 <= a < 65:
    print("Grade awarded: 4")
else:
    print("Grade awarded: F")

"""
Problem: A shipping company charges its customer based on the weight of goods and the distance of shipping. A discount is given based on the distance of shipping as follows:
distance < 250km, no discount 
250km ≤ distance < 500km, 10% discount
500km ≤ distance < 1000km, 15% discount
1000km ≤ distance < 2000km, 20% discount
2000km ≤ distance < 3000km, 35% discount
3000km ≤ distance, 50% discount
The shipping cost is calculated based on the following equation: 
cost = baseprice * weight * distance * (1 - discount).
Write a program that takes as inputs the baseprice, weight, and distance, and prints the shipping cost to be charged to the customer.
Example:
How much is the base price? 0.01
What is the weight? 200
What is the distance? 1000
The shipping cost is 1600.0

"""

baseprice = float(input("How much is the base price?"))
weight = float(input("What is the weight?"))
distance = float(input("what is the distance?"))

if distance < 250:
    dis = 0
elif distance < 500:
    dis = 10
elif distance < 1000:
    dis = 15
elif distance < 2000:
    dis = 20
elif distance < 3000:
    dis = 35
else:
    dis = 50
discount = dis / 100
cost = baseprice * weight * distance * (1 - discount)
print("The shipping cost is : ", cost)

"""
Problem: Write a program that takes as input 3 integers and outputs them in descending order.
Examples:
Integer 1? 3
Integer 2? 10
Integer 3? 2
Sorted: 10 3 2

"""

list1 = []
a = int(input("Enter 1st number "))
b = int(input("Enter 2nd number "))
c = int(input("Enter a 3rd number "))

list1.append(a)
list1.append(b)
list1.append(c)

print(sorted(list1, reverse=True))
