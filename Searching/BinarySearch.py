# ---------------Binary Search-----------

'''
🧠 Core idea

Binary Search works on a sorted array.

Instead of checking every element, we repeatedly cut the search area in half.

Example:

numbers = [1, 3, 5, 7, 9, 11, 13]
target = 11

             ↓
[1, 3, 5, 7, 9, 11, 13]
             ↑
           middle

7 < 11, so we discard everything on the left:

[9, 11, 13]
    ↑

Now 11 > 9, so discard 9:

[11, 13]
 ↑

Found 11 ✅
'''
# The three variables
# left = 0
# right = len(numbers) - 1

# Find the middle:

# mid = (left + right) // 2

# Then:

# if numbers[mid] == target:
#     return mid
# elif numbers[mid] < target:
#     left = mid + 1
# else:
#     right = mid - 1

# Complete function
# def binary_search(numbers, target):
#     left = 0
#     right = len(numbers) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if numbers[mid] == target:
#             return mid

#         elif numbers[mid] < target:
#             left = mid + 1

#         else:
#             right = mid - 1

#     return -1

'''
Complexity

Time: O(log n) ⚡
Space: O(1)

Why O(log n)?

Because every step cuts the search space roughly in half:

16 → 8 → 4 → 2 → 1

'''

'''
⚠️ Critical rule

Binary Search requires the data to be sorted:

[1, 3, 5, 7, 9, 11]    ✅
[1, 7, 3, 9, 2, 11]     ❌
'''

'''
🎯 Your turn

Implement binary_search() yourself using the pattern above.

Test:

numbers = [1, 3, 5, 7, 9, 11, 13]

print(binary_search(numbers, 11))  # 5
print(binary_search(numbers, 6))   # -1
'''

def binary_search(numbers  , target):
    left = 0 
    right = len(numbers) - 1

    while left <= right :
        mid = (left + right) // 2 

        if numbers[mid] == target:
            return mid 
    
        elif numbers[mid] < target:
            left = mid + 1 

        else:
            right = mid - 1

    return -1 

numbers = [1,3,5,7, 9,11,13]

print(binary_search(numbers , 11))
print(binary_search(numbers , 6))


# ------------------Binary Search Completed---------------------