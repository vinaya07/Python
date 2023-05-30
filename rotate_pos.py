"""
Problem: Write a program with a function that given a list of numbers, rotate the numbers so the first number becomes the last, and the rest of the numbers move one position forward. Do the rotation iteratively until the list of numbers returns to its initial form.
Input a list: 1 2 3 4
[1, 2, 3, 4]
[2, 3, 4, 1]
[3, 4, 1, 2]
[4, 1, 2, 3]
[1, 2, 3, 4]
"""

input_list = input("Input a list: ").split()


def rotation(nums):
    for i in range(len(nums) + 1):
        rotated = nums[i:] + nums[:i]
        result = rotated[:]
        final_result = [int(x) for x in result]
        print(final_result)


rotation(input_list)