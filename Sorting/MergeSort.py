# -----------Merge Sort-----------

'''
Now we're getting into the important O(n log n) sorting algorithms. 🔥

🧠 Core idea

Merge Sort uses Divide and Conquer:

Divide the array into smaller pieces → sort them → merge them back together.

Example:

[8, 3, 5, 4, 7, 6, 1, 2]
1. Divide
[8, 3, 5, 4]       [7, 6, 1, 2]

[8, 3] [5, 4]      [7, 6] [1, 2]

[8] [3] [5] [4]    [7] [6] [1] [2]

Eventually, every piece has one element.

A single element is already sorted.
'''

'''
2. Merge

Now we combine two sorted pieces.

[8] + [3]

Compare:

3 < 8

So:

[3, 8]

Then:

[5] + [4] → [4, 5]

Eventually:

[3, 8] + [4, 5]

Compare the front elements:

3 < 4 → take 3
4 < 8 → take 4
5 < 8 → take 5
8 → take 8

Result:

[3, 4, 5, 8]

And we continue merging until the entire array is sorted.
'''

'''
🔑 The two parts

Merge Sort really has two operations:

DIVIDE
   ↓
Split array recursively
   ↓
CONQUER
   ↓
Merge sorted halves

The merge step is the most important part to understand.

'''
# Python implementation

'''
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2

    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
'''
# nums = [8, 3, 5, 4, 7, 6, 1, 2]
# def merge_sort(nums):
#     if len(nums) <= 1 :
#         return nums

#     mid = len(nums) // 2  

#     left = merge_sort(nums[:mid])
#     right = merge_sort(nums[mid:])

#     result = []
#     i = 0 
#     j = 0 

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1 

#         else:
#             result.append(right[j])
#             j += 1 

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

# print(merge_sort(nums))

'''
Complexity

Time: O(n log n)

Why?

Splitting creates about log n levels.
Each level processes n elements during merging.

So:

n x log n = O(n log n)

Space: O(n) for the typical array implementation because we create merged arrays.

'''
'''
🆚 Why Merge Sort matters

Compared with the first three:

Algorithm	Average Time
Bubble Sort	O(n²)
Selection Sort	O(n²)
Insertion Sort	O(n²)
Merge Sort	O(n log n)

Merge Sort is therefore much more scalable for large datasets.
'''

'''
Exactly. 🔥

For:

[8, 3, 5, 4]

mid = 2, so:

left  → [8, 3]
right → [5, 4]

Then each half is divided again:

[8, 3] → [8] [3]
[5, 4] → [5] [4]

Now every piece has one element, so we start merging.

For example:

[8] + [3]

Compare 8 and 3:

3 < 8

So:

[3, 8]

And:

[5] + [4] → [4, 5]

Then:

[3, 8] + [4, 5]

becomes:

[3, 4, 5, 8]
'''

'''
Perfect. Your Merge Sort is 100% correct.

You implemented both critical parts correctly:

1. Divide
left = merge_sort(nums[:mid])
right = merge_sort(nums[mid:])

You recursively split until:

len(nums) <= 1
2. Merge
while i < len(left) and j < len(right):

Then you compare the front elements and take the smaller one:

if left[i] <= right[j]:
    result.append(left[i])
else:
    result.append(right[j])

And finally:

result.extend(left[i:])
result.extend(right[j:])

That last part is important because one side may still have elements after the other side is exhausted.

Your output:

[1, 2, 3, 4, 5, 6, 7, 8]
🔒 Merge Sort = DONE
Best: O(n log n)
Average: O(n log n)
Worst: O(n log n)
Space: O(n) for this implementation
Strategy: Divide and Conquer

 the divide → recursively sort → merge process. ✅
'''

# ----------merge Sort Completed------------