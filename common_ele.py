"""
Problem: Given two lists, write a program with a function that takes these two lists as the input arguments and returns the list of all the elements in the first list that occur in the second list. The returned list shall not contain duplicate elements. Your main program will allow the user to enter two lists of numbers and end the program by inputting a blank line for list 1.
List 1: 1 3 3 6
List 2: 3 4 2 1 2 1 3
Output: [1, 3]
List 1: 3 4 2 1 2 1 3
List 2: 5 6 7 8
Output: []
List 1:
"""
def duplicates(a, b):
    # res = set(a) & set(b)
    res = set(a).intersection(b)
    # final_res = [x for x in list(res)]
    final_res = [int(x) for x in list(res) if x != ' ']
    # print("Output:", list(res))
    print("Output:", final_res)


while True:
    list1 = input("List 1:")
    if list1 == "":
        break
    list2 = input("List 2:")
    duplicates(list1, list2)

# duplicates(list1, list2)