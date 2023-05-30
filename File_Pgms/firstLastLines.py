"""Problem: Write a program that prompts for the name of a file, then prints the first two lines
and the last two lines of the file.
File name: yesterday.txt
Output:
Yesterday Once More
When I was young
I would sing to then
And I’d memorize each...
"""
f = open(input("File name: "))
line = f.readlines()
fl = line[:2]
ll = line[-2:]
print("Output:")
for line in fl:
    print(line.strip())
for line in ll:
    print(line.strip())

f.close()