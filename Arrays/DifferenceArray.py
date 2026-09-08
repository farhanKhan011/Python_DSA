# ----------Difference Array----------

'''
The Difference Array is basically the reverse idea of Prefix Sum.

Prefix Sum is useful when you have many range-sum queries.

Difference Array is useful when you have many range updates.

Example

Suppose:

numbers = [0, 0, 0, 0, 0]

We want to add 5 to every element from index 1 through 3:

[0, 5, 5, 5, 0]

The naive way changes 3 elements.

With a difference array, we mark only the start and end of the update:

start: index 1 → +5
after index 3: index 4 → -5

So the difference array becomes:

[0, 5, 0, 0, -5]

Then taking the prefix sum of that difference array produces:

[0, 5, 5, 5, 0]
'''

'''
The core rule

For an update:

Add value from index L to R

we do:

diff[L] += value
diff[R + 1] -= value

Then calculate the prefix sum of diff.
'''

'''
first exercise

Start with:

numbers = [0, 0, 0, 0, 0]

Apply:

Add 3 to indexes 1 through 3

Your final result should be:

[0, 3, 3, 3, 0]
Rules
Use a difference-array approach.
Don't directly modify indexes 1, 2, and 3.
Use the L and R boundary idea.
Then reconstruct the final array using prefix sums.
'''
# arr = [0,0,0,0,0]
# arr[1] = 3
# arr[4] = -3

# print(arr)

# for i in range(1 ,len(arr)):
#     arr[i] += arr[i -1]
# print(arr)

'''
Complexity
Building/updating difference array: O(1) per range update
Reconstructing with prefix sum: O(n)
Extra space: O(1) in your implementation because you're modifying the array itself.

✅ Difference Array fundamentals: DONE.
'''
