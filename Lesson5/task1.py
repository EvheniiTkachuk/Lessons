# #The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

from random import randint as rand

s = []
i = 1
while i <= 10:
    s.append(rand((10**9), (10**10) - 1))
    print(f'{i}. {s[i-1]}')
    i += 1
maxElem = max(s)
print(f'Max list item at position {s.index(maxElem) + 1} and has matters {max(s)}')
