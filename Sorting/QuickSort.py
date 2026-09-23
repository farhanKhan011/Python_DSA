# -----------Quick Sort------------- 

'''
Quick Sort is another Divide and Conquer algorithm, like Merge Sort, but the way it divides the array is different.

🧠 Core idea: Pivot

Choose one element as a pivot.

Then rearrange the array so:

smaller elements | pivot | larger elements

Example:

[7, 2, 9, 4, 5]

Choose 5 as the pivot:

[2, 4] | 5 | [7, 9]

Now independently sort [2, 4] and [7, 9].
'''

'''
The process
Choose pivot
     ↓
Partition the array
     ↓
Everything smaller → left
Everything larger  → right
     ↓
Recursively quick-sort both sides
Example
[8, 3, 5, 4, 7, 6, 1, 2]

Suppose pivot = 2.

After partitioning:

[1] | 2 | [8, 3, 5, 4, 7, 6]

Then we repeat on the right side.
'''

'''
Complexity

Average:

O(n log n)

Worst case:

O(n²)

The worst case can happen when the pivot repeatedly produces very unbalanced partitions, such as:

[1, 2, 3, 4, 5]

if we repeatedly choose the smallest or largest element as the pivot.

Space is typically O(log n) for recursion with reasonably balanced partitions, though the worst-case recursion depth can reach O(n).
'''
'''
🆚 Merge Sort vs Quick Sort
	Merge Sort	Quick Sort
Average	O(n log n)	O(n log n)
Worst	O(n log n)	O(n²)
Main idea	Split → merge	Pivot → partition
Typical extra array space	O(n)	Low/in-place possible

Important: Quick Sort's performance depends heavily on pivot selection and partitioning.
'''

'''
🎯 Let's understand partition first

Take:

[7, 2, 9, 4, 5]

Choose:

pivot = 5

We want:

[smaller than 5] | 5 | [larger than 5]

So tell me:

Which numbers go to the left of 5, and which go to the right?

Today 10:41 PM
the 4 and 2 will go to the left of 5 and the 7 and 9 will go to the right of 5 

Exactly. 🔥 100% correct.

With:

[7, 2, 9, 4, 5]
pivot = 5

We get:

[2, 4] | 5 | [7, 9]

The important point is that partitioning doesn't necessarily sort the left and right sides. It only puts them on the correct side of the pivot.

So:

[2, 4]   → both < 5
[7, 9]   → both > 5

Then Quick Sort recursively works on:

[2, 4]
[7, 9]
🔑 Quick Sort mental model
Choose pivot
     ↓
Partition
     ↓
[smaller] | pivot | [larger]
     ↓
Recursively sort both sides
'''

'''
🎯 Your task: Write quick_sort(numbers) yourself.

Use:

numbers = [8, 3, 5, 4, 7, 6, 1, 2]

Expected:

[1, 2, 3, 4, 5, 6, 7, 8]
'''

nums = [8, 3,5, 4, 7, 6, 1, 2]

def quickSort(nums):
    if len(nums) == 1 :
        return nums
    pivot = nums[-1]
    result = []
    for num in nums:
        if num < pivot:
            left = num 

        else:
            right = num     

   





