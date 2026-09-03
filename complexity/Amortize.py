# -------------Amortize complexity----------------

'''
. What does "Amortized" mean?

Amortized analysis asks:

If an operation is sometimes expensive, how expensive is it on average over a long sequence of operations?

Important: amortized complexity is NOT the same as average-case complexity.

We'll use Python lists because they're a perfect example.
'''

# append() Looks Like O(1)
# numbers = []

# numbers.append(10)
# numbers.append(20)
# numbers.append(30)
# numbers.append(40)

'''
Usually, adding an element to the end is:
O(1)
because Python can put the new element into an available position
'''


'''
But Sometimes append() Is Expensive

Imagine the internal storage is full:

Before:

[10][20][30][40]
 ↑              ↑
elements       no room

Now you do:

numbers.append(50)

Python may need to:

Allocate a larger block of memory.
Copy the existing elements.
Add 50.

Conceptually:

Old:
[10][20][30][40]

        ↓ resize

New:
[10][20][30][40][50][ ][ ][ ]

Copying n elements can take:

O(n)

So append() can occasionally be O(n).
''' 

'''
Then Why Do We Say append() Is O(1) Amortized?

Because resizing doesn't happen every time.

Imagine:

append → cheap
append → cheap
append → cheap
append → expensive resize
append → cheap
append → cheap
append → cheap
append → expensive resize

Most operations are cheap.
The expensive resizing operations are spread across many cheap operations.
Over a long sequence of appends, the average cost per operation stays constant.
Therefore:
list.append() → O(1) amortized
'''

'''
Very Important Distinction

For Python's list.append():

Typical/amortized → O(1)
Occasional worst case → O(n)

So if an interviewer asks:

"What's the amortized complexity of appending to a dynamic array?"

Answer:

O(1) amortized.
'''

'''
6. Think About It Like This

Imagine you have to pay:

$1
$1
$1
$10
$1
$1
$1
$20

Some payments are expensive, but when you spread the total cost across all operations, the cost per operation remains small.

That's the basic intuition behind amortized analysis.

'''

