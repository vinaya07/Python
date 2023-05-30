"""
Problem: Given two lists, write a program with a function that merges these two lists in descending order. Your main program will allow the user to enter two lists of numbers and end the program by inputting a blank line for list 1. You are not allowed to concatenate the two lists into a new list and then call the built-in sort() function to sort the new list in descending order. But you are allowed to sort the two lists in descending order before merge. Don’t worry about the complexity of the merging algorithm.

List 1: 1 3 3 6
List 2: 1 4 5
[6, 5, 4, 3, 3, 1, 1]
List 1: 100
List 2: 1 1 3
[100, 3, 1, 1]

"""


def merge(a, b):
    # res = [x for n in (a, b) for x in n] //list comprehensive method
    for i in b:
        a.append(i)
    res = sorted(a, reverse=True)
    final_res = [int(x) for x in res]
    print(final_res)


while True:
    list1 = input("List 1:").split()
    if len(list1) == 0:
        break
    list2 = input("List 2:").split()
    merge(list1, list2)
