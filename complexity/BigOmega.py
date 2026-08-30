# ----------Big Omega-----------

'''
What is Big-Ω?

Big-Ω describes the lower bound of an algorithm's growth.

In simple words:

Big-O → upper bound
Big-Ω → lower bound

Think:

Big-O      → "At most / upper growth"
Big-Ω      → "At least / lower growth" 
'''
# Simple Example
# numbers = [10, 20, 30, 40, 50]

# for number in numbers:
#     print(number)
'''
This loop has to process every element.
So its complexity is:
O(n)
Ω(n)
Its growth is tightly tied to n.
'''

# Searching is Where Ω Becomes Interesting
# Consider Linear Search:
# def search(numbers, target):
#     for i in range(len(numbers)):
#         if numbers[i] == target:
#             return i

#     return -1
'''
Suppose:

numbers = [10, 20, 30, 40, 50]
target = 10

We find it immediately:

10
↑
1 check

So the best case is:

Ω(1)

But if:

target = 50

we may have to check everything:

10 → 20 → 30 → 40 → 50

That's n checks.

The worst case is:

O(n)

So linear search has:

Best case  → Ω(1)
Worst case → O(n)
'''
'''
Consider:

def find_number(numbers, target):
    for number in numbers:
        if number == target:
            return True

    return False

For:

numbers = [10, 20, 30, 40, 50]
Question:

What is the Big-Ω of this algorithm if the target is the first element?

And what is the Big-O if the target is the last element or doesn't exist?

Give me both and explain why.

'''
# if target is the first element the the omega is constant , the big O is linear as the n increases it will search for all the n  

'''
One more Ω question

Consider:

def example(numbers):
    for number in numbers:
        print(number)

What is its Big-Ω?

Think: what's the minimum amount of work this loop has to do when numbers contains n elements?
'''
# the big omega is linear as n increase we might have to check for all 

# ----------------Big Omega Completed------------------



