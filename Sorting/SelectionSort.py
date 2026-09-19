# -------------Selection sort--------------

'''
Selection Sort works differently from Bubble Sort.

🧠 Core idea

Instead of repeatedly swapping neighbors, we:

Find the smallest element in the unsorted portion and put it at the beginning.

Example:

[5, 3, 8, 1, 2]
 ↑
start

Find the smallest element:

[5, 3, 8, 1, 2]
          ↑
          1

Swap it with the first element:

[1, 3, 8, 5, 2]

Now 1 is finished.

Next, look only at:

[3, 8, 5, 2]

Smallest is 2 → put it at position 1:

[1, 2, 8, 5, 3]

Continue until sorted.
'''

# nums =[3,4,2,1,5]
# def selectionSort(nums):
#     n = len(nums)

#     for i in range(n):
#         min_index = i

#         for j in range(i + 1 , n): 
#             if nums[j] < nums[min_index] :  
#                 min_index = j 
#         nums[i] , nums[min_index] = nums[min_index] , nums[i] 
#     return nums 

# print(selectionSort(nums))

'''
Complexity
Best: O(n²)
Average: O(n²)
Worst: O(n²)
Space: O(1)

Unlike optimized Bubble Sort, Selection Sort still does the searching work even if the array is already sorted.
'''           

'''
Bubble vs Selection

Bubble Sort:

Compare neighbors → swap

Selection Sort:

Find minimum → swap once

Selection Sort therefore performs relatively few swaps, which can matter when swaps/writes are expensive.
'''

'''
practice : 
🎯 Your turn

Given:

[7, 4, 9, 2, 5]

After one Selection Sort pass, what will the array be?

Think: find the smallest element in the entire array, then swap it with the first element.

Today 11:39 PM
so to find the smallest element the 2 is the  smallest so it will be swap with  7 so it will become like [2,4,9,7,5]

Exactly! 🔥 100% correct.

Starting with:

[7, 4, 9, 2, 5]

Find the smallest → 2.

Swap 2 with the first element 7:

[2, 4, 9, 7, 5]

Now the first position is sorted/finalized.

🔒 Selection Sort key idea
Find minimum
     ↓
Swap with current position
     ↓
Move current position forward
     ↓
Repeat

And remember:

Best: O(n²)
Average: O(n²)
Worst: O(n²)
Space: O(1)
Fewer swaps than Bubble Sort
'''

# -----------Selection Sort Completed----------