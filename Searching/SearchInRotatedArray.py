# --------------Search in Rotated Array---------------

'''
🧠 What's a rotated sorted array?

Start with a sorted array:

[1, 3, 5, 7, 9, 11, 13]

Rotate it:

[7, 9, 11, 13, 1, 3, 5]

It is still made from a sorted array, but the order is "broken" at one point.

The goal is still to find a target in O(log n).

The key observation

At every step, at least one half is sorted.

Example:

[7, 9, 11, 13, 1, 3, 5]
 ↑           ↑        ↑
left        mid      right

If:

numbers[left] <= numbers[mid]

then the left half is sorted.

Otherwise, the right half is sorted.

Example
[7, 9, 11, 13, 1, 3, 5]
 ↑           ↑
 L           M

Left half:

[7, 9, 11, 13]

is sorted.

Now ask:

Is my target inside this sorted range?

For target 11:

7 <= 11 <= 13

✅ Yes → search left.

Otherwise → search right.

Python pattern
'''

# def search_rotated(numbers, target):
#     left = 0
#     right = len(numbers) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if numbers[mid] == target:
#             return mid

#         # Left half is sorted
#         if numbers[left] <= numbers[mid]:

#             if numbers[left] <= target < numbers[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1

#         # Right half is sorted
#         else:

#             if numbers[mid] < target <= numbers[right]:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#     return -1

'''
Time: O(log n)
Space: O(1)

This standard version assumes distinct values. Duplicate values require an additional case.
'''

'''
🎯 Your turn

Don't code yet. For:

numbers = [6, 7, 8, 1, 2, 3, 4, 5]
target = 3

At the beginning:

left = 0
right = 7

What is mid, and which half is sorted?

3

✅ Correct!

mid = (0 + 7) // 2
mid = 3

So:

index:   0  1  2  3 | 4  5  6  7
         6  7  8  1 | 2  3  4  5
                    ↑
                   mid

Now determine which half is sorted:

numbers[left] <= numbers[mid]
6 <= 1

❌ False.

Therefore, the right half is sorted:

[2, 3, 4, 5]

🎯 Your turn: Is the target 3 inside that sorted right-half range [2, 5]?

Just answer yes or no.

Today 12:47 AM
yes

Exactly. ✅

Since 3 is inside the sorted range [2, 5], we keep the right half:

left = mid + 1

So:

left = 4
right = 7

Now we have:

[2, 3, 4, 5]
 ↑     ↑
 L     R

Next:

mid = (4 + 7) // 2

🎯 What is mid now?

5

🔥 Correct!

mid = (4 + 7) // 2
mid = 5

At index 5:

numbers[5] = 3

And our target is:

target = 3

So:

numbers[mid] == target

✅ Found!

The function returns:

5
🔒 The pattern to remember

For a rotated array:

Check mid 🎯
Determine which half is sorted
Check whether target lies inside that sorted half
Search that half; otherwise search the other half

Time: O(log n)
Space: O(1)

Now write the complete search_rotated() function yourself using the pattern we just learned. Send it over and I'll check it.
'''

# Practice Question 


def search_rotated(numbers , target):
    left = 0 
    right = len(numbers) - 1 

    while left <= right:
        mid = (left + right) // 2 
        
        if numbers[mid] == target :
            return mid 

        if numbers[left] <= numbers[mid]:

            if numbers[left] <= target < numbers[mid]:
                right = mid -1 
            else:
                left = mid + 1
        else:
            if numbers[mid] < target <= numbers[right]:
                left = mid + 1 
            else:
                right = mid - 1 

    return -1

numbers = [12, 15, 18, 2, 4, 6, 8, 10]
target = 6
search_rotated(numbers , target)
print(search_rotated(numbers , target))

# ----------------Search In Rotated Array Completed----------------------