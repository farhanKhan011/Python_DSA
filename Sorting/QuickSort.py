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
We have:

nums = [8, 3, 5, 4, 7, 6, 1, 2]
1. First: choose a pivot

Let's make the last element the pivot.

pivot = nums[-1]

So:

[8, 3, 5, 4, 7, 6, 1, 2]
                         ↑
                       pivot

Therefore:

pivot = 2
2. Partition

Now we compare every other number with 2.

Our goal:

numbers smaller than pivot | pivot | numbers greater than pivot

For our array:

8 > 2 → right
3 > 2 → right
5 > 2 → right
4 > 2 → right
7 > 2 → right
6 > 2 → right
1 < 2 → left

So we get:

[1] | 2 | [8, 3, 5, 4, 7, 6]

🔥 This is partitioning.

Notice something important:

We did NOT sort [8, 3, 5, 4, 7, 6].

We only separated numbers based on the pivot.

3. Now Quick Sort the two sides

We now have:

[1] | 2 | [8, 3, 5, 4, 7, 6]

The left side:

[1]

is already sorted.

So we recursively Quick Sort:

[8, 3, 5, 4, 7, 6]

Choose its last element as pivot:

[8, 3, 5, 4, 7, 6]
                   ↑
                 pivot

Pivot = 6.

Partition:

[3, 5, 4] | 6 | [8, 7]

Again, we haven't completely sorted anything yet.

Then:

[3, 5, 4]

Choose 4:

[3] | 4 | [5]

And:

[8, 7]

Choose 7:

[] | 7 | [8]

Eventually everything becomes:

[1] | 2 | [3] | 4 | [5] | 6 | [7] | 8

Therefore:

[1, 2, 3, 4, 5, 6, 7, 8]
'''
'''
🧠 Now look at the recursive structure

This is the part you were missing.

Quick Sort essentially does:

def quick_sort(numbers):

    choose pivot

    partition into:
        left
        pivot
        right

    quick_sort(left)
    quick_sort(right)

    combine:
        left + pivot + right

That's the whole algorithm.
'''

'''
Let's write a SIMPLE version

Forget the complicated in-place implementation for now.

We'll use extra lists because I want you to understand the algorithm first.
'''
# def quickSort(nums):
#     if len(nums) <= 1:
#         return nums
#     pivot = nums[-1]
#     left = []
#     right = []

#     for num in nums[:-1]:
#         if num < pivot:
#             left.append(num)
#         else:
#             right.append(num)

#     return quickSort(left) + [pivot] + quickSort(right)

# nums = [8, 3, 5, 4, 7, 6, 1, 2]

# print(quickSort(nums))


'''
Quick Sort — Interview Level
1. The core idea

Quick Sort is:

Divide → Partition → Recursively Sort

Choose a pivot, then rearrange the array so:

elements smaller than pivot | pivot | elements larger than pivot

Then recursively do the same thing on the left and right portions.

The important difference from our previous code:

❌ We created new left and right lists.

left = []
right = []

That costs extra memory.

For interview-level implementation, we should learn in-place partitioning.
'''    

'''
In-place Quick Sort
We'll use the Lomuto partition scheme first because it's easier to reason about correctly.
'''
# def quick_sort(nums, low, high):
#     if low < high:
#         pivot_index = partition(nums, low, high)

#         quick_sort(nums, low, pivot_index - 1)
#         quick_sort(nums, pivot_index + 1, high)


# def partition(nums, low, high):
#     pivot = nums[high]
#     i = low

#     for j in range(low, high):
#         if nums[j] < pivot:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1

#     nums[i], nums[high] = nums[high], nums[i]

#     return i

'''
Understand partition() — this is the important part

Suppose:

nums = [8, 3, 5, 4, 7, 6, 1, 2]
                              ↑
                            pivot

Pivot = 2.

We maintain:

i = low

i represents the position where the next smaller-than-pivot element should go.

j scans the array.

for j in range(low, high):

Whenever:

nums[j] < pivot

we swap it into position i.

After the scan, we put the pivot at i.

So the final guarantee is:

[values < pivot] pivot [values >= pivot]

Then we return the pivot's final index.

That's the key idea you need to be able to explain verbally in an interview.
'''
'''
4. Complexity

For a reasonably balanced partition:

T(n) = 2T(n/2) + O(n)

Therefore:

Average: O(n log n)

Best case:

O(n log n)

But if the pivot repeatedly produces extremely unbalanced partitions:

T(n) = T(n-1) + O(n)

then:

Worst case: O(n²)

Space:

Partition itself: O(1) extra space
Recursion stack:
average: O(log n)
worst: O(n)

So don't simply say "Quick Sort is O(1) space" in an interview. The recursion stack matters.
'''
'''
The Google-level trade-off

The important interview question isn't:

"Can you memorize Quick Sort?"

It's:

"How would you make Quick Sort perform reliably?"

One major problem is pivot selection.

If we always choose:

pivot = nums[high]

and the input is already sorted:

[1, 2, 3, 4, 5, 6, 7]

we can repeatedly get:

0 elements | pivot | 6 elements
0 elements | pivot | 5 elements
0 elements | pivot | 4 elements
...

That's O(n²).

So in production/interview discussion, you should know strategies such as:

Randomized pivot

Choose a random pivot instead of consistently choosing the last element.

This makes consistently bad partitions much less likely.

Median-of-three

Choose a pivot based on:

first
middle
last

and use their median.

This can improve practical behavior on certain inputs.

6. One more important thing

For Python, you normally wouldn't implement Quick Sort in real production code just to sort a list.

Python's built-in:

sorted(nums)

and:

nums.sort()

use Timsort, which is highly optimized.

But for DSA interviews, you absolutely need to understand and implement Quick Sort because the interviewer may ask you to.
'''

'''
exercise

Implement this yourself:

nums = [10, 7, 8, 9, 1, 5]

Write an in-place Quick Sort using the Lomuto partition approach, without creating left and right arrays.
'''
nums = [10, 7, 8, 9, 1, 5]

def quickSort(nums , low , high ):
    if low < high :
        pivot_index = partition(nums , low , high) 

        quickSort(nums, low , pivot_index -1 )
        quickSort(nums, pivot_index + 1 , high)

def partition(nums , low , high):
    pivot = nums[high]
    i = low 

    for j in range(low , high):
        if nums[j] < pivot:
            nums[i] , nums[j] = nums[j] , nums[i]

            i += 1
    nums[i] , nums[high] = nums[high] , nums[i]

    return i 

quickSort(nums, 0 , len(nums) -1 )

print(nums)

'''
Complexity
Best: O(n log n)
Average: O(n log n)
Worst: O(n²)
Partition extra space: O(1)
Recursion stack: O(log n) average, O(n) worst
'''
# -------------Quick Sort Completed-----------