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

