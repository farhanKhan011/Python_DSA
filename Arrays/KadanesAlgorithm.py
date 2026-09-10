# --------------Kadane's Algorithm---------------

'''
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

The best contiguous portion is:
[4, -1, 2, 1]

Its sum is:
6
'''

'''
The core idea

At every position, ask:

Should I extend the current subarray, or start a new one here?

That gives us:

current = max(number, current + number)

And separately track the best sum we've seen:

best = max(best, current)

So the basic pattern is:

current = numbers[0]
best = numbers[0]

for number in numbers[1:]:
    current = max(number, current + number)
    best = max(best, current)

For the example:

[-2, 1, -3, 4, -1, 2, 1, -5, 4]

Kadane eventually finds:

6
Complexity
Time: O(n) ✅
Extra Space: O(1) ✅
'''

'''
Your challenge 😈

Given:

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Find the maximum contiguous subarray sum using Kadane's Algorithm.

Expected answer:

6

Don't use sum() to test every possible subarray.
'''
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
current = numbers[0]
best = numbers[0]

for number in numbers[1:]:

  current  =  max(number , current + number )
  best =  max(best , current)

print(best)
    
'''
And the subarray producing it is:
[4, -1, 2, 1]

Complexity
Time: O(n) ✅
Extra Space: O(1) ✅

One important thing you got right: initializing with numbers[0] instead of 0. This makes Kadane's algorithm correctly handle arrays containing only negative numbers.

Example:

[-5, -2, -8]

The answer should be -2, not 0.

'''

