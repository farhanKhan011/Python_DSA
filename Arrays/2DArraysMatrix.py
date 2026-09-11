# ------------Matrix / 2D Arrays-------------

'''
A 2D array is basically an array containing arrays.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Think of it as a grid:

1  2  3
4  5  6
7  8  9

We access an element using:

matrix[row][column]

For example:

matrix[1][2]

gives:

6

because row 1 is:

[4, 5, 6]

and column 2 is 6.
'''

'''
Traversing a 2D array

Usually we use nested loops:

for row in matrix:
    for value in row:
        print(value)

Output:

1
2
3
4
5
6
7
8
9

Or when you need the indexes:

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        print(matrix[r][c])
'''

'''
Complexity

For a matrix with R rows and C columns:

Time: O(R x C)

because every cell is visited once.
'''

'''
Your first challenge 🧠

Given:

matrix = [
    [3, 7, 2],
    [8, 1, 5],
    [4, 6, 9]
]

Use nested loops to find the largest value without using max().

Expected:

9

Also think about the complexity.
'''
# matrix = [
#     [3, 7, 2],
#     [8, 1, 5],
#     [4, 6, 9]
# ] 

# find = matrix[0][0]

# for r in matrix:
#     for c in r:
#         if c > find:
#             find = c
# print(find)

'''
For a square matrix of n × n:

O(n × n) = O(n²) ✅

But for a general matrix with R rows and C columns, we should say:

O(R × C)

Because the number of rows and columns don't necessarily have to be equal.

For example:

3 × 5 → 15 cells
100 × 2 → 200 cells

So don't automatically call every 2D traversal O(n²).

Space

Your algorithm uses only:

find
r
c

No additional structure proportional to the matrix.

Extra Space: O(1) ✅
'''
'''
One more important 2D-array concept

Before we move on, you need to be comfortable with row/column traversal, because it's going to show up everywhere later—graphs, grids, DP, etc.

Try this:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Calculate the sum of each row and print:

6
15
24

Use nested loops. No sum().
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


for i in matrix :
    row_sum = 0 
    for j in i:
        row_sum += j
    print(row_sum)



'''
Complexity

For an R x C matrix:

Time: O(R x C) ✅
Extra Space: O(1) ✅
'''

# -----------2D Array / Matrix Completed-----------
