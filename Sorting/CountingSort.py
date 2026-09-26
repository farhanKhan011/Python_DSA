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
nums = [4, 2, 2, 8, 3, 3, 1]

def countingSort(nums):
    max_value  = max(nums)
    count = [0] * (max_value + 1)
    # count = [0,0,0,0,0,0,0,0,0]

    for num in nums:
        count[num] += 1  
    result = []

    for value in range(len(count)):
        for _ in range(count[value]):
            result.append(value)
    return result 
        
print(countingSort(nums))
