# ---------------Binary Search on Answer-----------------

'''
It looks different from normal Binary Search, but the idea is still:

Search a sorted range by repeatedly cutting it in half.

The difference is that we're often not searching for an element.

We're searching for the minimum or maximum possible answer.

Simple example

Suppose you need to find the minimum speed needed to finish a job.

Possible speeds:

1  2  3  4  5  6  7  8  ...

We create a condition:

Can I finish at this speed?

Maybe:

speed 3 → ❌
speed 4 → ❌
speed 5 → ✅
speed 6 → ✅
speed 7 → ✅

Notice the pattern:

❌ ❌ ❌ ❌ ✅ ✅ ✅
            ↑
        first valid answer

That's what makes Binary Search on Answer possible.
'''

'''
🧠 The key pattern

We have a monotonic condition:

False False False True True True

or:

True True True False False False

Then Binary Search finds the boundary.
'''

# Example
# Find the minimum number from 1 to 10 that is at least 7.

# def binary_search_answer():
#     left = 1
#     right = 10

#     while left < right:
#         mid = (left + right) // 2

#         if mid >= 7:
#             right = mid
#         else:
#             left = mid + 1

#     return left

# Answer: 7

'''
Notice something important:

We aren't doing:

numbers[mid] == target

Instead, we're asking:

if mid >= 7:

That's the fundamental difference.

Normal Binary Search
Search → an element
Binary Search on Answer
Search → the answer/range of possible answers

Time: O(log n) if checking the condition is O(1).
'''

'''
Your first real exercise 🎯

Find the minimum number from 1 to 20 that is greater than or equal to 13 using Binary Search on Answer.

Write:

def find_answer():
     .
     .
     .

'''
def find_answer():
    left = 1
    right = 20

    while left < right:
        mid = (left + right ) // 2

        if mid >= 13:
            right = mid
        else:
            left = mid + 1
    return left

print(find_answer())


'''
🔒 Lock this pattern in

For finding the minimum valid answer:

while left < right:
    mid = (left + right) // 2

    if condition(mid):
        right = mid
    else:
        left = mid + 1

return left

The key difference from normal Binary Search is:

Normal: search for an element.

Binary Search on Answer: search for the first value that satisfies a condition.

Time: O(log n)
Space: O(1)

'''

# ------------Binary Search On Answer Completed-------------