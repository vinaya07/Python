"""
Problem: Write a program with a function that given a list of numbers, returns True if and only if all of the numbers in the list form an arithmetic progression, that is the difference between any two successive numbers in the list is the same. Your main program should read a file containing space-separated numbers as test lists, print each list and the outcome after calling the function.
File name: numbers.txt
[1 2 3 4] True
[10 20 30 40] True
[10 9 8 7] True
[2 7 8 3] False
[1 2 3 5] False
"""

def arithmetic(e):
    src = e[1] - e[0]
    for i in range(len(e) - 1):
        if not (e[i + 1] - e[i] == src):
            return False
    return True


f = open(input("File Name: "))
lines = f.readlines()
for line in lines:
    res = [int(i) for i in line.split(' ') if i.isdigit()]
    print(res, arithmetic(res))

f.close()