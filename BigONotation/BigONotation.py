# ------------------------Big O Notation-------------------

'''
What is Big-O?
Big-O describes how an algorithm's resource usage grows as the input size n grows.
For example:
for number in numbers:
    print(number)
If numbers has n elements, the loop runs n times.
So: O(n)
Big-O lets us compare algorithms without caring about the exact machine, CPU speed, or milliseconds.
'''
'''
Big-O is About Growth
Suppose Algorithm A performs:
10n operations
and Algorithm B performs:
n² operations
For small inputs, the difference might not matter much.
But as n becomes huge:
10n      → grows linearly
n²       → grows quadratically
Eventually n² becomes much more expensive.
That's why we care about the growth rate.
'''
'''
Big-O is About Growth
Suppose Algorithm A performs:
10n operations
and Algorithm B performs:
n² operations
For small inputs, the difference might not matter much.
But as n becomes huge:
10n      → grows linearly
n²       → grows quadratically
Eventually n² becomes much more expensive.
That's why we care about the growth rate.
'''
'''
Drop Constants
Suppose:
for number in numbers:
    print(number)
for number in numbers:
    print(number)
We already established:
O(n) + O(n)
= O(2n)
Big-O drops the constant:
O(2n) → O(n)
Similarly:
O(5n)   → O(n)
O(100n) → O(n)
O(n/2)  → O(n)
Why?
Because we're interested in how the algorithm scales, not the exact multiplier.
'''
'''
Drop Lower-Order Terms
Consider:
O(n² + n)
As n becomes large, n² grows much faster than n.
So:
O(n² + n) → O(n²)
Likewise:
O(n³ + n² + n) → O(n³)
and:
O(n + log n) → O(n)
The largest-growing term dominates.
'''
'''
Common Big-O Order
From fastest growth to slowest growth:
O(1)
   ↓
O(log n)
   ↓
O(n)
   ↓
O(n log n)
   ↓
O(n²)
   ↓
O(n³)
   ↓
O(2ⁿ)
   ↓
O(n!)
Actually, "fastest" here means fastest-growing cost, so the bottom ones become expensive much more quickly as n increases.
For Google-level DSA, you'll repeatedly encounter:
O(1), O(log n), O(n), O(n log n), O(n²)
'''
# Example: O(n + 5)
# def example(numbers):
#     for number in numbers:
#         print(number)

#     print("hello")
#     print("hello")
#     print("hello")
#     print("hello")
#     print("hello")
'''
Complexity:
Loop → O(n)
Five print statements → O(1)
Therefore:
O(n + 1)
→ O(n)
The constant work doesn't matter as n grows. 
'''
'''
Example: O(3n² + 2n + 10)
Suppose your analysis gives:
O(3n² + 2n + 10)
Drop constants:
O(n² + n + 1)
Then keep the dominant term:
O(n²)
So:
O(3n² + 2n + 10) → O(n²)
'''
'''
Important: Big-O Isn't Always Literally the Exact Number of Operations
For example:
for i in range(n):
    print(i)
You might technically have loop setup, comparisons, increments, etc.
But we don't write:
O(3n + 2)
We simplify it to:
O(n)
That's the whole purpose of asymptotic notation.
'''

'''
🧠 Practice
Question 1

What is the Big-O?

def example(numbers):
    for number in numbers:
        print(number)

    for number in numbers:
        print(number)

    print("Done")

Think:

first loop  → ?
second loop → ?
print       → ?
total       → ?

Question 2
Simplify:
O(5n² + 3n + 20)

Question 3
Simplify:
O(2n + log n + 100)
'''
# Q1 : first loop -> O(n) , second loop -> O(n) , print -> O(1) , total -> O(n + n + 1 ) = O(n) linear, 
# Q2 : O(5n^2 + 3n + 20 ) so drop the constants -> O(n^2 + n ) keeping the dominant -> O(n^2)
# Q3 : O(2n + log n + 100 ) -> drop constant so we get O(n + log n ) now drop the lower order log n so answer is  O(n)

'''
🔥 Let's make it slightly harder

Analyze this function:

def example(numbers):
    n = len(numbers)

    for i in range(n):
        print(numbers[i])

    for i in range(n):
        for j in range(n):
            print(numbers[i], numbers[j])

    print(numbers[0])

Break it down:

First part       → ?
Nested part      → ?
Last print       → ?
Overall Big-O    → ?
'''
# first part -> O(n) cuz iterate over all the length or elements of numbers. 
# Nested part -> O(n^2) cuz it iterate so n x n = n^2 
# Last print -> O(1) constant cuz it just have to print the value on index 0 , no more operations.
# Overall Big-O -> O(n + n^2 + 1) -> (n + n^2) -> n^2 cuz drop constant then take dominant.


# ----------Big-O Completed---------