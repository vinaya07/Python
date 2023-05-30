"""
Problem: The Unix tool wc counts the numbers of characters, words and lines in a file.
Write your own version of wc that prompts for the name of the file to read, then prints the counts.
Assume a word may contain letters, digits, symbols and their mixture, but not space. Hyphenated words,
e.g. large-scale, shall be considered as one word.
Output:
File name: python.txt
Characters: 1227
Words: 176
Lines: 10
"""

f = open(input("File name:"), "r")
num_chars = num_words = num_lines = 0
for line in f:
    num_lines += 1
    num_chars += len(line)
    line = line.strip()   #remove whitespaces
    words = line.split()  #split into list using whitespace
    num_words += len(words)
print("Characters:", num_chars)
print("Words:", num_words)
print("Lines:", num_lines)
f.close()