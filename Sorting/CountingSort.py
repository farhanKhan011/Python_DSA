# ----------Counting Sort-----------

'''
Counting Sort is fundamentally different from the comparison-based sorts we've learned.
'''
'''
Instead of comparing elements like:

a < b

it uses the value of each element as an index to count how many times that value appears.

Example
nums = [4, 2, 2, 8, 3, 3, 1]

First find the range:

min = 1
max = 8

Create a counting array:

value:  0 1 2 3 4 5 6 7 8
count:  0 1 2 2 1 0 0 0 1

Meaning:

1 appears 1 time
2 appears 2 times
3 appears 2 times
4 appears 1 time
8 appears 1 time

Then reconstruct:

[1, 2, 2, 3, 3, 4, 8] 

'''
# def countingSort(nums):

#     max_value = max(nums)
#     count = [0] * (max_value + 1)

#     for num in nums:
#         count[num] += 1

#     result = []

#     for value in range(len(count)):
#         for _ in range(count[value]):
#             result.append(value)
#     return result

# nums = [4, 2, 2, 8, 3, 3, 1]
# print(countingSort(nums))

'''
Complexity

If:

n = number of elements
k = range of values

Then:

Time: O(n + k)
Space: O(k)

This can be faster than O(n log n) sorting when k is reasonably small.

For example:

[2, 1, 4, 3, 2, 1, 3]

Great candidate.

But:

[1, 999999999]

would require a huge counting array, despite having only two elements.

So the key interview insight is:

Counting Sort is useful when the values are integers and the value range is not excessively larger than the number of elements.

'''

'''
1. The problem with the basic version

The basic implementation assumes:

0 <= num <= max_value

So this fails conceptually for:

[-5, -2, 0, 3, -2]

because we can't use -5 as a normal list index.

The solution is to use an offset based on the minimum value.

2. Handling negative numbers

For:

nums = [-5, -2, 0, 3, -2]

We have:

min = -5
max = 3
range = 9

We create:

count = [0] * (max_value - min_value + 1)

Then map each number to an index:

index = num - min_value

For example:

num = -5
index = -5 - (-5) = 0

num = -2
index = -2 - (-5) = 3

num = 3
index = 3 - (-5) = 8

So every value gets a valid index.
'''

# def counting_sort(nums):

#     minValue = min(nums)
#     maxValue = max(nums)

#     count = [0] * (maxValue - minValue + 1)

#     for num in nums :
#         count[num - minValue] += 1 

#     result = []

#     for i in range(len(count)):
#         for _ in range(count[i]):
#             result.append(i + minValue)

# nums = [-5, -2, 0, 3, -2]
# print(counting_sort(nums))

'''
Now the important interview concept: Stability

A sorting algorithm is stable if elements with equal keys maintain their original relative order.

For example, imagine:

(John, 2)
(Ali, 1)
(Sara, 2)

Sorting by the number:

(Ali, 1)
(John, 2)
(Sara, 2)

John was before Sara originally, and remains before Sara.

That's stability.

Why do we care?

Because stable Counting Sort is useful inside Radix Sort.

4. How stable Counting Sort works

Instead of immediately reconstructing values from the counts, we calculate prefix positions.

Suppose:

nums = [4, 2, 2, 8, 3, 3, 1]

After counting, we transform counts into cumulative positions.

Conceptually:

count[value] = number of elements <= value

Then we traverse the original array from right to left.

For each element:

Find its position using count.
Put it into the output array.
Decrease its count.

This preserves the relative ordering of equal elements.

A standard stable implementation is:
'''
def countingSort(nums):
    if not nums:
        return nums 

    minValue = min(nums)
    maxValue = max(nums)

    count = [0] * (maxValue - minValue + 1)

    for num in nums:
        count[num - minValue] += 1

    #converting a count to a cumulative positions 
    for i in range( 1, len(count)):
        count[i] += count[i -1] 

    result = [0] * len(nums)


    #Traversing backwards for stability 
    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        index = num - minValue

        count[index] -= 1
        result[count[index]] = num

    return result

nums =  [4, 2, 2, 8, 3, 3, 1]
print(countingSort(nums))

'''
Why backwards?
This line:  for i in range(len(nums) - 1, -1, -1):

is what allows equal elements to preserve their original ordering.
That's a detail worth knowing for interviews.

5. When should you actually use Counting Sort?
Think:
Are the values integers?
        ↓
Is the value range relatively small?
        ↓
Yes → Counting Sort may be excellent

Example:
scores: 0-100
ages: 0-120
small integer IDs
Potentially excellent.
But:
[1, 500000000]
Counting Sort is a poor choice because the range k is enormous compared with n.

Complexity:

For n elements and value range k:
Time: O(n + k)
Space: O(n + k) for the stable implementation because we maintain the count array and output array.
And importantly:
Counting Sort is not comparison-based, which is why it can beat the O(n log n) comparison-sorting lower bound when its assumptions are satisfied.
'''

# --------------Counting Sort Completed---------------