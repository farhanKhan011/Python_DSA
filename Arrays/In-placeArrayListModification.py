# ------------------In-Place Array/List Modification----------------------

'''
Modify the existing list without creating another list.

Why? Because sometimes you can solve a problem in O(1) extra space instead of O(n).

Example: Reverse a list

Suppose:

numbers = [10, 20, 30, 40, 50]

We want:

[50, 40, 30, 20, 10]

A simple approach is creating another list:

new_list = []

for number in numbers:
    ...

That uses:
O(n) extra space.
But we can modify the original list directly.
'''
'''
Two Pointers

Use two indexes:

[10, 20, 30, 40, 50]
 ↑                    ↑
left                 right

Swap them:

[50, 20, 30, 40, 10]

Move inward:

[50, 40, 30, 20, 10]
     ↑          ↑

Continue until they meet.

Python:
numbers = [10, 20, 30, 40, 50]

left = 0
right = len(numbers) - 1

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]

    left += 1
    right -= 1

print(numbers)

Output:

[50, 40, 30, 20, 10]
Complexity

We perform roughly n/2 swaps:

Time → O(n)

But we don't create another list:

Extra Space → O(1)

This is a very important pattern called Two Pointers.

Your Challenge 🔥

Given:
numbers = [1, 2, 3, 4, 5, 6, 7]
Reverse it in-place.

Rules:

❌ Don't use [::-1]
❌ Don't use .reverse()
❌ Don't create new_list
✅ Use two pointers
✅ Extra space should be O(1)
'''
# numbers = [1,2,3,4,5,6,7]
# left = 0 
# right  = len(numbers) - 1 

# while left < right : 
#     numbers[left] , numbers[right] = numbers[right] , numbers[left]
#     left += 1
#     right -= 1

# print(numbers)

'''
Complexity
Time: O(n)
Extra Space: O(1) ✅
Pattern: Two Pointers
'''

# Next challenge: remove all occurrences of a given value in-place using O(1) extra space.
'''
Challenge 🔥
Given:

numbers = [3, 7, 2, 7, 5, 7, 9, 4]
target = 7

Remove all occurrences of target in-place.

Rules:

❌ Don't create new_list
❌ Don't use list comprehensions
❌ Don't use .remove()
❌ Don't use .filter()
✅ Modify numbers itself
✅ Extra space must be O(1)

Expected result:

[3, 2, 5, 9, 4]

Your turn. 😈
'''
numbers = [3, 7, 2, 7, 5, 7, 9, 4]
target = 7 
write_index = 0 

for index , number in enumerate(numbers):
    if number != target:
        numbers[write_index] = number
        write_index += 1 
numbers = numbers[:write_index]
print(numbers)

'''
Complexity
Time: O(n) ✅
Extra space: O(1) for the removal algorithm itself
Pattern: Write Pointer / Two Pointers ✅

One interview detail: technically, the slicing line creates a new list,
 so if the interviewer means strictly no new allocation whatsoever, 
 we'd need to handle the final size differently. But your core algorithm is exactly right.
'''

# ----------Inplace operations completed------------ 
 