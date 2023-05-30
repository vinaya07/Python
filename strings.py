"""
Problem: Write a program that reads strings (without digits or symbols in the string) typed by the user until an empty string is entered. For each string, convert all words to lowercase, then sort and print the words into descending order lexicographically. Hint: use split function to split a string into a list, then sort it with a method.
output:
Enter a string: Three Rings for the eleven kings under the sky
Output: under three the the sky rings kings for eleven
Enter a string: Nine for Mortal Men doomed to die
Output: to nine mortal men for doomed die

"""
while True:
    str = input("Enter a string : ")

    if str == "":
        break

    words = [word.lower() for word in str.split()]
    words.sort(reverse=True)

    print("Output: ", end=" ")
    for word in words:
        print(word, end=" ")
    print()

"""
Problem: Write a program that allows the user to enter two lists of integers, calculate the sum of the first and the last integers in each list, and print the larger sum. In the event of a tie, print Same. When there is only one integer in the list, the sum is the integer itself.
List 1: 1 2 3 4 5
List 2: 5 6 7
Output: 12
List 1: 4 3 10 1
List 2: 9
Output: 9
List 1: 4 3 2 1
List 2: 1 2 3 4
Output: Same
"""
list1 = list(map(int, input("List 1: ").split()))
list2 = list(map(int, input("List 2: ").split()))


def sum(n):
    if len(n) == 1:
        return n[0]
    else:
        return n[0] + n[-1]


sum1 = sum(list1)
sum2 = sum(list2)

if sum1 > sum2:
    print("Output:", sum1)
elif sum2 > sum1:
    print("Output:", sum2)
else:
    print("Output:Same")

"""
Problem: We’ll say that a lowercase ’g’ in a string is ”happy” if there is another ’g’ immediately to its left or right. Write a function to print True if all the g’s in the given string are happy, otherwise, print False.

Output:
String: xggt
Happy?: True

String: abgsx
Happy?: False

String: g
Happy?: False

String: brggsomr
Happy?: True
"""
str = input("String: ")


def happy(s):
    if s.count('g') == 1:
        return False
    for i in range(len(s)):
        if s[i] == 'g' and s[i - 1] != 'g' and s[i + 1] != 'g':
            return False
    return True


print("Happy?", happy(str))

"""
Problem: Write a program that allows the user to enter the marks of 5 students in 4 courses, and outputs the highest average marks for students and courses. Hint: Consider 2 dimensional lists, i.e. the element of a list is a list.
Output:
Student 1 (courses 1-4): 50 60 70 60 
Student 2 (courses 1-4): 100 90 87 90
Student 3 (courses 1-4): 70 100 90 90
Student 4 (courses 1-4): 30 65 50 50
Student 5 (courses 1-4): 58 50 74 43
The highest average mark of students: 91.75
The highest average mark of courses: 74.2
"""

marks = []
for i in range(5):
    print(f"Student {i + 1} (courses 1-4): ", end="")
    student_marks = [int(a) for a in input().split()]
    marks.append(student_marks)

student_averages = []
for i in range(5):
    average = sum(marks[i]) / 4
    student_averages.append(average)

highest_student_average = max(student_averages)

course_averages = []
for i in range(4):
    total = 0
    for j in range(5):
        total += marks[j][i]
    average = total / 5
    course_averages.append(average)

highest_course_average = max(course_averages)

print("The highest average mark of students: {:.2f}".format(highest_student_average))
print("The highest average mark of courses: {:.2f}".format(highest_course_average))

"""
Problem: Write a program that prompts for and reads strings until a string that starts with the letter “A” is entered (inclusive), then prints the longest string that was entered.  Sample run:
Enter a string: Jaypher said, ’It’s safer
Enter a string: you’ve lemons in your head;
Enter a string: First to eat, a pound of meat, 
Enter a string: Find then to go at once to bed.
Enter a string: Eating meat is half the battle, 
Enter a string: Will you hear the Lemons rattle!
Enter a string: If you don’t, you’ll always moan,
Enter a string: In a Lemoncolly tone;
Enter a string: For there’s nothing half so dreadful, 
Enter a string: As Lemons in your head.
Longest was: 'For there’s nothing half so dreadful,'

"""
longestString = ""
a = " "
while a[0] != 'A':
    a = input("Enter a String: ")
    if len(a) > len(longestString):
        longestString = a

print(f"Longest was:'{longestString}'")

"""
Write a program with a function that converts all numerical digits in a string to underline.

output:
Input a string? Australia has 59,736 km coastal line
Output: Australia has __,___ km coastal line

Input a string? 10 4 2
Output: __ _ _
"""


def conversion(result):
    r = "_"
    for i in result:
        if i.isdigit():
            result = result.replace(i, r)
    return result


# string = str(input("Input a String? "))
string = input("Input a String? ")
print("Output: " + conversion(string))

"""
Problem: Given starting and ending years, write a program with a function to calculate the number of days from starting year to ending year inclusive.  Hints: Write a function to check leap year. Sample code is in the lecture notes of Section 10: Type Bool and Boolean Expressions. Sample run:
Year 1? 1980
Year 2? 2022
Number of days: 15706

"""


def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True
    return leap


def total_days(year1, year2):
    days = 0
    for year in range(year1, year2 + 1):
        if is_leap(year):
            days += 366
        else:
            days += 365
    return days


year1 = int(input("Year 1? "))
year2 = int(input("Year 2? "))
print("Number of days:", total_days(year1, year2))
