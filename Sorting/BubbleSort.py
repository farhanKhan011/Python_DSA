# ----------Bubble Sorting-----------

'''
🧠 What is Bubble Sort?

Bubble Sort repeatedly compares neighboring elements and swaps them if they're in the wrong order.

Example:

[5, 3, 8, 1]

5 > 3 → swap
[3, 5, 8, 1]

5 < 8 → no swap
[3, 5, 8, 1]

8 > 1 → swap
[3, 5, 1, 8]

Notice what happened:

The largest element "bubbled" to the end.

After one complete pass:

[3, 5, 1, 8]
             ↑
          largest

Then we repeat for the remaining unsorted portion.

The basic algorithm

For each pass:

compare adjacent elements
        ↓
if left > right
        ↓
swap them
        ↓
continue
'''

# def bubble_sort(nums):
#     n = len(nums)

#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if nums[j] > nums[j + 1 ]:
#                 nums[j],nums[j+1] = nums[j+1] , nums[j]
#     return 

# numbers = [5, 3, 8, 1, 2]
# print(bubble_sort(numbers))
            
'''
⚠️ Important: When would you use Bubble Sort?

For real large-scale software or Google interview problems, Bubble Sort is generally not the practical choice because O(n²) is slow.

You learn it because it teaches an important foundation:

Repeated local comparisons and swaps can gradually produce a globally sorted array.

Later, we'll compare it with Merge Sort, Quick Sort, etc., and understand why you'd choose one over another.
'''

# Worst: O(n²)
# Average: O(n²)
# Best with early-stop optimization: O(n)
# Space: O(1)
# Mainly useful for learning; rarely chosen for large real-world datasets.

# ----------------Bubble Sort Completed--------------
