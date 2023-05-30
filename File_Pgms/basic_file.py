"""
Write a program that prompts for the names of a source file to read and a target file to write, and copy the content of the source file to the target file, but with all lines starting with a digit removed.
"""

source = input("Enter the source file name: ")
target = input("Enter the target file name: ")

fs = open(source, "r")
ft = open(target, "w")

for line in fs:
    if not line.strip().startswith(tuple(map(str, range(10)))):
        ft.write(line)

fs.close()
ft.close()

"""
Write a program that prompts for the name of the file to read, then count and print how many times the string “file” appears in the file. The string count() method is not allowed. 
"""

f = open(input("Enter the file name: "), "r")
count = 0

for line in f:
    words = line.split()

    for word in words:
        if word.lower() == "file":
            count += 1

print(f"The string 'file' appears {count} times in the file.")

f.close()

"""
Write a function that, given a list argument, returns True if the list contains no duplicates (every element is unique), False otherwise. For example, if the list is [1, 2, 3, 4, 5], return True. If the list is [1, 2, 3, 4, 4], return False. 

Assume the function argument is valid. Do not handle erroneous arguments. You are asked to write a function, not a complete program.
"""


def has_no_duplicates(lst):
    unique_ele = set()

    for element in lst:
        if element in unique_ele:
            return False
        else:
            unique_ele.add(element)

    return True


"""
Write a program that prompts for the names of a source file to read and a target file to write, and copy the content of the source file to the target file, but with all lines starting with an uppercase letter ‘A’ removed. Finally, close the files. 
"""
fs = open(input("Enter the source file name: "), "r")
ft = open(input("Enter the target file name: "), "w")

for line in fs:
    if not line.strip().startswith('A'):
        ft.write(line)

fs.close()
ft.close()


"""
Write a program that prompts for the name of the file to read, then count and print the number of words that contain only lowercase letters.
"""

f = open(input("Enter the file name: "), "r")
count = 0

for line in f:
    words = line.split()

    for word in words:
        if word.islower():
            count += 1

print(f"The number of words containing only lowercase letters: {count}")

f.close()


"""
Write a program that prompts for the names of a source file to read and a target file to write, and copy the content of the source file to the target file, but with all lines containing the colon symbol ':' removed. Finally, close the files.
"""

fs = open(input("Enter the source file name: "), "r")
ft = open(input("Enter the target file name: "), "w")

for line in fs:
    if ':' not in line:
        ft.write(line)

fs.close()
ft.close()

