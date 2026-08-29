# --------Time Complexity----------

'''
1. What is Time Complexity?
Time complexity tells us:
How does the amount of work an algorithm performs grow as the input gets bigger?
It does not mean exactly how many seconds your program takes.
'''
# for example:
# numbers = [10,20,30,40,50]
# for number in numbers:
#     print(number)
'''
If there are 5 numbers → the loop runs 5 times.
If there are 1,000 numbers → it runs 1,000 times.
If there are 1,000,000 numbers → it runs 1,000,000 times.
So the amount of work grows with n.
We describe this as:
O(n)
where n = size of the input.
'''

'''
2. Why Do We Care?

Imagine two algorithms:
Algorithm A'''
numbers = [10,20,30,40,50]

# for number in numbers:
    # print(number)
'''
Work grows roughly like:
n
Algorithm B
'''
for x in numbers:
    for y in numbers:
        print(x, y)
'''
If n = 5:
5 × 5 = 25
If n = 1,000:
1,000 × 1,000 = 1,000,000
The second algorithm grows much faster.
'''
'''
What is n?
n simply represents the input size.
For a list:
numbers = [1, 2, 3, 4, 5]
n = 5
For:
numbers = [1, 2, 3, ..., 100000]
n = 100000
So when we say:
O(n)
we're basically saying:
"The work grows proportionally to the size of the input."
'''
# The Most Important Complexities
'''
O(1)          Constant
O(log n)      Logarithmic
O(n)          Linear
O(n log n)    Linearithmic
O(n²)         Quadratic
O(2ⁿ)         Exponential
O(n!)         Factorial
'''

# O(1) — Constant
# Example is :
numbers = [10,20,30,40,50]
print(numbers[2])
'''
No matter whether the list contains:
5 elements
100 elements
1,000,000 elements
we directly access index 2.
The amount of work doesn't grow with n.
Therefore: O(1)
'''
# O(n) — Linear
# Example 
# numbers = [10,20,30,40,50]
# for number in numbers:
#     print(number) 
'''
The loop visits every element.

n = 5       → 5 operations
n = 100     → 100 operations
n = 1000    → 1000 operations

Therefore: O(n)
'''
# O(n²) — Quadratic
numbers = [1,2,3,4,5]

# for x in numbers:
#     for y in numbers:
#         print(x,y)
'''
We have a loop inside another loop.
If:
n = 5
roughly:
5 x 5 = 25
If:
n = 100
then:
100 x 100 = 10,000
Therefore:  O(n²)
This pattern is extremely important to recognize.
'''
'''
Compare these carefully:

Two separate loops:

n + n = 2n → O(n)

Nested loops:

for x in numbers:
    for y in numbers:
n x n = n² → O(n²)
Remember this rule 🔥

Separate loops → usually ADD their complexities.
Nested loops → usually MULTIPLY their complexities. 
'''
'''
Separate loops:
O(n) + O(n) = O(2n) = O(n)

Nested loops:
O(n) x O(n) = O(n²)
'''
# _______________________________________________
'''
O(log n)

Consider:

def example(n):
    while n > 1:
        n = n // 2

Suppose:
n = 16
16 → 8 → 4 → 2 → 1
Only 4 iterations.
For n = 32:
32 → 16 → 8 → 4 → 2 → 1
Only 5 iterations.
'''
'''
Only 5 iterations.
The input doubles, but the number of operations increases by only about one.
That's O(log n).
This pattern is extremely important because Binary Search uses it.
'''

'''
the four most important basic patterns:

Pattern	Complexity
Fixed amount of work	O(1)
One loop through n	O(n)
Nested loops	O(n²)
Repeatedly divide by 2	O(log n)
'''
'''
the core Time Complexity rules:
Fixed work → O(1)
One full traversal → O(n)
Nested traversal → O(n²)
Repeated division → O(log n)
Separate operations → add them
Final complexity → keep the dominant term
'''

# ----------------Time Complexity completed)--------------------