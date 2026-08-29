# -------------List and Array----------------

'''
Python Lists and Arrays
In Python, lists are the built-in data structure that serves as a dynamic array.
Lists are ordered, mutable, and can contain elements of different types.
A Python list stores multiple values in one ordered collection.

'''
# numbers = [10, 20, 30, 40, 50]
'''
think of it like:

Index:     0    1    2    3    4
           ↓    ↓    ↓    ↓    ↓
List:     [10] [20] [30] [40] [50]

Each element has an index, starting from 0.
'''
# print(numbers[0])  # 10
# print(numbers[3])  # 40
'''
Why Lists Matter in DSA
A huge number of DSA problems start with an array.
In Python, the closest general-purpose equivalent is the list.
For example:

numbers = [5, 2, 8, 1, 9]

we might need to:

Find an element
Find maximum/minimum
Reverse the list
Sort it
Insert elements
Delete elements
Traverse every element
Search for something
'''
'''
Creating a List 
'''
# numbers = [ 20 , 40 , 60 , 80 , 100]
# emopty list 
# marks = []
# diffrerent data types are allowed
# data = [10, "hello", 3.14, True]

# Accessing Elements
# numbers = [10,20,30,40,50]
# print(numbers[0])
# print(numbers[1])
# print(numbers[3])

# Negative indexing
# print(numbers[-1])
# print(numbers[-2])

'''
Changing List elements
Lists are mutable, meaning we can change their elements.
'''
# num = [23,34,54,23]
# num[0] = 24
# print(num)

# Traversing a List
# This is extremely important in DSA

# myNum = [2,4,6,8,10]

# for i in myNum:
#     print(i)

# italso work with indexes:
# for i in range(len(myNum)):
#     print(myNum[i])

# The second approach becomes very useful when solving algorithm problems.

'''
Python lists come with several built-in algorithms (called methods),
to perform common operations like appending, sorting, and more.
'''
# Adding Elements
# append()   , Adds to the end:
# marks = [56,76,87,56,89]
# marks.append(90)
# print(marks)

# insert()
# Adds at a specific position:
# marks = [56,76,87,56,89]
# marks.insert(0,68)
# print(marks)

# Removing Elements
# pop()
# numbers = [1,2,3,4,5,0]
# numbers.pop()
# print(numbers)
# removes the last element
# You can also specify an index:
# numbers.pop(3)

# remove() , remove element
# numbers.remove(5)


# Important Operations
# You should know these very well:
'''
len(numbers)
numbers.append(x)
numbers.pop()
numbers.pop(i)
numbers.insert(i, x)
numbers.remove(x)
numbers[i]
numbers[i] = x
Also:

numbers.reverse()
numbers.sort()
'''
'''
The Most Important DSA Concept Here: Complexity

Don't worry if this isn't completely clear yet—we'll have a dedicated Time Complexity topic later.

For now, remember:

Operation	Typical Complexity
numbers[i]	O(1)
Change numbers[i]	O(1)
append()	O(1) amortized
pop() from end	O(1)
insert(0, x)	O(n)
pop(0)	O(n)
Search by value	O(n)
remove(x)	O(n)

Why is inserting at the beginning expensive?

Before:
[10, 20, 30, 40]

insert 5 at index 0

After:
[5, 10, 20, 30, 40]

The existing elements have to shift.
'''
'''
Create Algorithms
Sometimes we want to perform actions that are not built into Python.
Then we can create our own algorithms.
'''
# DSA Problem

'''
Your First DSA Problem
Don't look for a solution yet.
Given:
Write a program that finds the largest number.
Don't use:
max(numbers)
We want to practice the actual algorithmic thinking.
'''
'''
Think:
numbers = [12, 45, 7, 89, 23, 56]
Start with:
largest = ?
Then compare each number.
Write the code yourself.
'''

# Solve these 3 problems:

# Problem 1
# Find the largest number without max().
# numbers = [12, 45, 7, 89, 23, 56]
# largest = numbers[0] 
# for number in numbers:
#     if number > largest:
#         largest = number
# print(largest)

# Problem 2
# Find the smallest number without min().
# numbers = [12, 45, 7, 89, 23, 56]
# smallest = numbers[0] 
# for number in numbers:
#     if number < smallest:
#         smallest = number
# print(smallest)

# Problem 3
# Count how many times 7 appears:
# numbers = [7, 2, 7, 5, 7, 9, 2, 7]
# counter = 0
# for number in numbers:
#     if number == 7:
#         counter += 1
# print(counter)

'''
Before moving away from Lists, let's do one slightly harder exercise:
Given:
numbers = [10, 20, 30, 40, 50]
Reverse the list WITHOUT using:
reverse()
slicing [::-1]
reversed()
For example:
[10, 20, 30, 40, 50]
             ↓
[50, 40, 30, 20, 10]
'''

# numbers = [10, 20, 30, 40, 50]
# a = -1
# newlist = []
# for i in numbers:
#     i = numbers[a]
#     a -= 1
#     newlist.append(i) 
# print(newlist) 
    # for i in numbers:
# isn't actually using i as the list element—you overwrite it immediately:
# i = numbers[a]
# So i isn't necessary.
# so the logic could be simplified to:
# a = -1
# newlist = []
# for _ in numbers:
#     newlist.append(numbers[a])
#     a -= 1
# print(newlist)

# numbers = [10, 20, 30, 40, 50]
# Print the list in reverse using positive indexes only.
'''
Rules:
No reverse()
No [::-1]
No negative indexes
No reversed()
Hint: the last index is len(numbers) - 1.
'''
# numbers = [10,20,30,40,50]
# a = 1
# mylist = []
# for _ in numbers:
#     mylist.append(numbers[len(numbers)-a])
#     a += 1
# print(mylist)    
'''
One final List challenge
Now let's combine what you've learned.

Given:
numbers = [4, 7, 2, 7, 9, 7, 3, 7]

Find:
1. The largest number
2. The smallest number
3. How many times 7 occurs
4. Create a new list containing the numbers in reverse order

Rules:
      Don't use:
      max()
      min()
      count()
      reverse()
      [::-1]
      reversed()

Do all four in one program.
'''    
numbers = [4, 7, 2, 7, 9, 7, 3, 7]
largest = numbers[0]
smallest = numbers[0]
newlist = []
counter = 0 
a = 1
for number in numbers:
    if number > largest :
        largest = number
    if number < smallest:
        smallest = number
    if number == 7:
        counter += 1
    newlist.append(numbers[len(numbers) - a])
    a += 1    
print('reversed list : ', newlist ,', maximum value in list : ', largest ,', minimum value in list : ', smallest ,', seven occurs :',counter )


# List/Array completed
