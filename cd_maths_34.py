""" You are given a ‘true’ string. String is called true if weight of string is multiple of 8. 
Your task is to tell whether a string can be declared True or Not. 
Weight of string is the sum of ASCII value of Vowel character(s) present in the string.

Input Description:
You are given as string ‘s’ in lower cases

Output Description:
Print 1 for true and 0 for false"""

# Input the string
s = input().strip()

# Define vowels and their ASCII values
vowels = 'aeiou'

# Calculate the weight of the string
weight = sum(ord(char) for char in s if char in vowels)

# Check if the weight is a multiple of 8
if weight % 8 == 0:
    print(1)
else:
    print(0)
