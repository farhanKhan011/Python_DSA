# --------------Sliding Window--------------

'''
What is Sliding Window?

Sliding Window is used when we need to work with a contiguous portion of an array/string.

Instead of repeatedly calculating the same elements, we maintain a "window" and slide it.

Example:

[2, 1, 5, 1, 3, 2]
 └─────┘
  window

Suppose we want the sum of every 3 consecutive elements.

First window:

2 + 1 + 5 = 8

Slide one position:

   [1, 5, 1]

Instead of calculating 1 + 5 + 1 from scratch:

old sum = 8
remove 2
add 1

8 - 2 + 1 = 7

That's the key idea:

Remove what leaves the window, add what enters the window.
'''
# Challenge 
'''
numbers = [2, 1, 5, 1, 3, 2]
k = 3

Find the maximum sum of any 3 consecutive elements.

Expected:

9

Rules:

❌ Don't calculate every window with sum()
❌ Don't create new lists
✅ Use Sliding Window
✅ O(n) time
✅ O(1) extra space
'''
numbers = [2, 1, 5, 1, 3, 2]
k = 3 
def sumSliding(numbers , k ):
    windowSum = sum(numbers[:k])
    max_sum = windowSum

    for i in range(len(numbers) -k ):
        windowSum = windowSum - numbers[i] + numbers[i + k]

        max_sum = max(max_sum , windowSum)
    return max_sum


print(sumSliding(numbers ,  k )) 


'''
Complexity
Time: O(n) ✅
Extra Space: O(1) ✅

And importantly, you used sum(numbers[:k]) only once to initialize the first window. That's perfectly fine for this challenge.
'''

# ----------------Sliding Window Completed---------------- 
