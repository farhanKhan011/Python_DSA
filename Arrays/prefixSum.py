# -----------------Prefix Sum---------------

'''
Prefix Sum is a technique for quickly calculating the sum of a range of an array.
'''

'''
Suppose:

numbers = [2, 4, 1, 5, 3]

The prefix sums are:

2
2 + 4 = 6
2 + 4 + 1 = 7
2 + 4 + 1 + 5 = 12
2 + 4 + 1 + 5 + 3 = 15 
prefix = [2, 6, 7, 12, 15]

The key idea is:

Each position stores the sum of everything before it, including itself.
'''

'''
Why do we need it?

Imagine you're asked:

What is the sum from index 1 to 3?

Without prefix sum:

4 + 1 + 5 = 10

You calculate those elements every time.

But with:

prefix = [2, 6, 7, 12, 15]

we can calculate the range sum extremely quickly.

For a range left → right:

prefix[right] - prefix[left - 1]

For 1 → 3:

prefix[3] - prefix[0]
= 12 - 2
= 10

That's the fundamental idea.
'''

'''
Complexity

Building the prefix array:

O(n) time

Range-sum query:

O(1) time

Extra space:

O(n)
'''
'''
first exercise 🔥

Given:

numbers = [5, 2, 7, 3, 6]

Create a prefix list manually using a loop.

Expected:

[5, 7, 14, 17, 23]

Don't use any library or built-in cumulative-sum function.
'''
# numbers = [5,2,7,3,6]
# prev = 0 
# for index , num  in enumerate(numbers):
#     next = num + prev
#     numbers[index] = next
#     prev += num
# print(numbers)
# Complexity : O(n) time and O(1) extra space because modified the original list

# Alternative
# numbers = [5, 2, 7, 3, 6]

# for i in range(1 , len(numbers) ):
#     numbers[i] += numbers[i - 1]
# print(numbers)

# ------------Prefix Sum Completed---------------
