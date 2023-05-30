"""Problem: Write a program that prompts for the names of a source file to read and a target file to write,
and copy the content of the source file to the target file, but with all empty lines removed, then output the number
of empty lines removed.
Output:
Source file name: string_doc.txt
Target file name: string_doc_nonempty.txt
Lines removed: 16
"""
src = open(input("Source file name: "), 'r')
tgt = open(input("Target file name: "), 'w')
count = 0
for line in src:
    if line.strip():
        tgt.write(line)
    else:
        count += 1


src.close()
tgt.close()
print("lines removed:", count)
