# b. Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.

from itertools import combinations
from function_exercises import calculate_tip
print(calculate_tip(100,0.2))

# 2. Read about and use the itertools module from the python standard library to help you solve the following problems:
# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
import itertools
print((len(list(itertools.product([1,2,3],'abc')))))

print((list(itertools.product([1,2,3],'abc'))))

# How many different combinations are there of 2 letters from "abcd"?
print((len(list(itertools.combinations('abc',2)))))

# How many different permutations are there of 2 letters from "abcd"?
print((len(list(itertools.permutations('abc',2)))))


import json
json.load(open('profiles.json'))

