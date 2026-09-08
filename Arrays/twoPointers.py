# -----------------Two Pointers----------------

'''
What is Two Pointers?

Instead of using one position/index, we maintain two positions that move through the array based on some condition.

The most common setup:

left = 0
right = len(numbers) - 1

Then:

while left < right:
    # do something
    left += 1
    right -= 1
000000000
Think:

        left →          ← right
[ 1, 2, 3, 4, 5, 6, 7 ]

The pointers move toward each other.
'''

'''
Example: Check if an array is a palindrome
numbers = [1, 2, 3, 2, 1]

left = 0
right = len(numbers) - 1

while left < right:
    if numbers[left] != numbers[right]:
        print(False)
        break

    left += 1
    right -= 1
else:
    print(True)

We compare:

1 ↔ 1
2 ↔ 2
3

Therefore:

True
'''

'''
Why is this better?

A common beginner approach might create a reversed copy:

numbers[::-1]

That requires O(n) extra space.

Two pointers need only:

left
right

So:

Time: O(n)
Extra Space: O(1)
'''

'''
Another important form

Two pointers don't always have to start at opposite ends.

They can also move in the same direction:

i →
j →
[ 1, 2, 3, 4, 5, 6 ]

This becomes especially useful for things like removing duplicates, merging arrays, and sliding-window-style problems.
'''

'''
Challenge 🔥

Given:

numbers = [1, 2, 3, 2, 1]

Use two pointers to determine whether the list is a palindrome.

Rules:

❌ Don't use [::-1]
❌ Don't use reversed()
❌ Don't create another list
✅ Use left and right
✅ O(n) time
✅ O(1) extra space

Expected output:
True
'''

# numbers = [1, 2, 3, 2, 1]
# left = 0
# right = len(numbers) - 1

# while left < right :
#     if numbers[left] != numbers[right]:
#         print(False)
#         break

#     left += 1
#     right -= 1

# else:
#     print(True)

'''
Complexity
Time: O(n)
Extra Space: O(1) ✅
'''

'''in Two pointers
we understand:

Opposite-direction pointers
Moving pointers based on conditions
In-place processing
Palindrome checking

some covered in other files while some here .
'''

# -------------------Two Pointers Completed----------------
