# -----------------Array/List Fundamentals-----------------

'''
What is an Array?

An array stores elements in an ordered sequence:

Index:    0    1    2    3    4
          ↓    ↓    ↓    ↓    ↓
        [10] [20] [30] [40] [50]

The important property is that elements have positions called indexes.
'''
'''
In traditional languages such as C++, arrays have a fixed size.

Python's list behaves more like a dynamic array:

numbers = [10, 20, 30]

numbers.append(40)

It can grow when needed.
'''
'''
Random Access

This is one of the most important properties of arrays.

numbers = [10, 20, 30, 40, 50]

print(numbers[3])

Python can directly access index 3.

numbers[3] → 40

Therefore:

Access by index → O(1)

It doesn't need to search through indexes 0, 1, 2 first.
'''

'''
Traversal

If you need to inspect every element:

for number in numbers:
    print(number)

You visit n elements.

Therefore:

Traversal → O(n)
'''

'''
Updating
numbers[2] = 100

Direct index update:

O(1)
'''

'''
Searching

Suppose:

numbers = [10, 20, 30, 40, 50]

and you want to find 40.

Without knowing its index, you may need:

10 → 20 → 30 → 40

Therefore, ordinary linear search is:

O(n)

We'll study searching properly later.
'''

'''
Insertion

This is where arrays become interesting.

Suppose:

[10, 20, 30, 40]

Insert 5 at the beginning:

[5, 10, 20, 30, 40]

The existing elements need to shift.

So insertion at the beginning is generally:

O(n)

But appending at the end of a Python list is:

O(1) amortized
'''

'''
Deletion

Same idea.

Removing the first element:

Before:
[10, 20, 30, 40]

After:
[20, 30, 40]

Elements have to shift.

So:

Delete from beginning → O(n)

Removing from the end:

numbers.pop()

is:

O(1)
'''

'''
Important Complexity Table
Operation	Complexity
Access arr[i]	O(1)
Update arr[i]	O(1)
Traverse	O(n)
Search	O(n)
Append	O(1) amortized
Insert at beginning	O(n)
Delete at beginning	O(n)
Pop from end	O(1)

This table is worth remembering.
'''

'''
First Array Problem

Don't use Python's built-in shortcuts.

Given:

numbers = [12, 5, 8, 20, 3, 15]

Write a function that returns the index of the largest element.

For example:

largest = 20
index = 3
Rules

Don't use:

max()
index()

Think in terms of:

largest value
      +
its index
'''

# def lgst():
#     numbers = [12,5 ,8 , 20 , 3  , 15]
#     largest = numbers[0]
#     largest_counter = 0
#     counter = 0
#     for number in numbers:
#         if number > largest:
#             largest = number
#             largest_counter = counter
#         counter += 1
            
#     print(largest_counter)
#     print(largest) 

# lgst()

        #  Alternative use enumurate function

# numbers = [12,5 ,8 , 20 , 3  , 15]
# largest = numbers[0]
        
# for i , number in enumerate(numbers):
#     if number > largest:
#         largest = number
#         largest_index = i
# print(largest_index)
# print(largest)

'''
Next challenge
Given:

numbers = [10, 4, 7, 10, 3, 10, 8]

Find the index of the first occurrence of the largest value.

Expected:

largest = 10
index = 0

Don't use max() or index().
'''

# numbers = [10, 4, 7, 10, 3, 10, 8]
# largest = numbers[0]
# largest_index = 0 
# for index , number in enumerate(numbers):
    
#     if number > largest:
#         largest = number
#         largest_index = index

# print(largest)
# print(largest_index)

'''
Complexity

Time: O(n) — you inspect every element.

Space: O(1) — index, number, largest, and largest_index are constant extra variables.
'''
'''
Next challenge: find the second largest distinct element without using sort(), max(), or converting the list to a set.
'''
# numbers = [10, 4, 7, 10, 3, 10, 8]
# largest = float('-inf')
# secondLargest = float('-inf')

# for number in numbers:
#     if number > largest:
#         secondLargest = largest
#         largest = number
#     elif number > secondLargest and number < largest:
#         secondLargest = number        
    
# print(largest)
# print(secondLargest)

'''
analysis
First loop   → O(n)
Second loop  → O(n)

Total time:
O(n) + O(n)
= O(2n)
= O(n) ✅

Space:

result → O(n)
total  → O(1)

Total:
O(n) + O(1)
= O(n) ✅
'''

# --------------Arrays/list completed-------------

