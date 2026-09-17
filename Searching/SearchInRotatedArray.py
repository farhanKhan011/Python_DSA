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

def search_rotated(numbers , target ):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2 

        if numbers[mid] == target:
            return mid 
        
        if numbers[left] <= numbers[mid]:

            if numbers[left] 



numbers = [9,11,13,1,3,5,7]
target = 11