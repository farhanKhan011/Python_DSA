# -------------Insertion Sort-------------

'''
Insertion Sort is like sorting cards in your hand.

You take one element at a time and insert it into its correct position among the elements already sorted.

🧠 Example
[5, 3, 8, 1]

Start by considering 5 sorted:

[5] [3, 8, 1]

Take 3:

5 > 3 → move 5 right

[3, 5, 8, 1]

Take 8:

8 > 5? No
→ stays

[3, 5, 8, 1]

Take 1:

8 → move right
5 → move right
3 → move right
1 → insert at beginning

[1, 3, 5, 8]
'''

'''
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        current = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > current:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = current

    return numbers
'''
# nums = [5,3,8,1]
# def insertion_sort(nums):

#     for i in range(1 , len(nums)):
#         current = nums[i]
#         j  = i -1 

#         while j >= 0 and nums[j] > current:
#             nums[j + 1] = nums[j] 
#             j -= 1
#         nums[j + 1] = current 
#     return nums

# print(insertion_sort(nums))


'''
Complexity
Best: O(n) — already sorted
Average: O(n²)
Worst: O(n²)
Space: O(1)
'''

'''
🔑 When is Insertion Sort useful?

It's particularly useful when the data is small or already nearly sorted. It can perform very well in those situations.

Think:

Bubble    → repeatedly swap neighbors
Selection → repeatedly find minimum
Insertion → take an element and insert it into the sorted portion
'''

'''
🎯 Your turn

Given:

[5, 2, 4, 6]

After inserting 2 into the sorted portion [5], what does the array become?

[2 , 5 , 4  , 6 ]
'''

'''
✅ Correct!

Starting with:

[5, 2, 4, 6]

The sorted portion is [5].

Take 2:

5 > 2

Move 5 right and insert 2:

[2, 5, 4, 6]

Exactly what you got. 🔥

One important thing to remember

Insertion Sort maintains a sorted portion on the left:

[ sorted | unsorted ]

After inserting 2:

[2, 5 | 4, 6]

Then we'd take 4, insert it into [2, 5], and continue.

🔒 Insertion Sort
Best: O(n)
Average: O(n²)
Worst: O(n²)
Space: O(1)
Good for small or nearly sorted data
'''

# -------Insertion Sort Completed-------------