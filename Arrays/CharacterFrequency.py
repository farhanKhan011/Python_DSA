# --------------Character Frequency------------

'''
Character frequency means counting how many times each character appears in a string.

Example:

text = "banana"

Frequency:

b → 1
a → 3
n → 2

The most common DSA approach is a hash map. In Python, that's a dictionary:

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

Result:

{'b': 1, 'a': 3, 'n': 2}
'''

'''
A shorter Python version is:

frequency[char] = frequency.get(char, 0) + 1

But understand the longer version first—the underlying pattern matters more than the shortcut.

Complexity

For a string of length n:

Time: O(n) average
Space: O(k), where k = number of distinct characters
'''

'''
Your challenge 🧠

Given:

text = "programming"

Create a dictionary containing the frequency of every character.

Expected:

{
    'p': 1,
    'r': 2,
    'o': 1,
    'g': 2,
    'a': 1,
    'm': 2,
    'i': 1,
    'n': 1
}

Use a loop and dictionary.
'''

# text = "programming"

# frequency = {}

# for char in text:

#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# print(frequency)

# or 

# for char in text:

#     frequency[char] = frequency.get(char , 0 ) + 1 

'''
text = "hello"

Find the first character that appears exactly once.

Expected:

h

Use your frequency dictionary approach.

'''
text = "hello"
frequency = {}

for char in text :
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
for char in text:
    if frequency[char] == 1:
        print(char)
        break 

# ----------------Character Frequency Completed-------------------