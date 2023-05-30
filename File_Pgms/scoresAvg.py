"""
Problem: Write a program that prompts for the name of a file containing numbers in each line,
prints the average of each line. Assume each line contains numbers only and they are separated by spaces.
Output:
File name: scores.txt
The average of line 1 is 60.0
The average of line 2 is 91.75
The average of line 3 is 48.75
The average of line 4 is 56.25

"""

f = open(input("File name: "))
lines = f.readlines()
line_num = 0
for line in lines:
    count = 0
    sum = 0
    line_num += 1
    for i in line.split(' '):
        count += 1
        sum += int(i)
    average = sum / count
    print(f"The average of line {line_num} is {average}")

f.close()