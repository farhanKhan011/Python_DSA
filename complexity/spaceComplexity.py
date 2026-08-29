# -----------------Space Complexity-----------------

'''
What is Space Complexity?
Space complexity = how much extra memory an algorithm needs as the input grows.
Time complexity asks:
How much work?
Space complexity asks:
How much extra memory?
'''

'''
O(1) Space
Example:
'''
# def example(numbers):
#     total = 0

#     for number in numbers:
#         total += number

#     return total
'''
We only create one extra variable:
total
Whether numbers contains 10 or 10 million elements, we're still using roughly the same extra memory.
So:
Space = O(1)
'''
# __________________________________________
'''
O(n) Space
Now look at this:
'''
# def example(numbers):
#     new_list = []
#     for number in numbers:
#         new_list.append(number)
#     return new_list
'''
If the input has:
n = 5
we create 5 new elements.
If: n = 1,000
we create 1,000 new elements.
So the extra memory grows with n.
Space = O(n) 
'''

'''
Important: Input Space vs Extra Space
This is VERY important.
Suppose:
'''
# def example(numbers):
#     total = 0

#     for number in numbers:
#         total += number
'''
The numbers list already exists. We generally don't count the input itself when discussing auxiliary/extra space.

We're asking:

How much additional memory did our algorithm create?

Here:

numbers → input
total   → extra memory

Therefore:

Auxiliary Space = O(1)
'''
'''
Another Example
'''
# def example(numbers):
#     result = []

#     for number in numbers:
#         result.append(number * 2)

#     return result
'''
The new result grows with the input.

Therefore:

Time  → O(n)
Space → O(n
'''

'''
Time and Space Can Be Different
For example:
'''
def find_max(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
'''
We inspect every element:
Time → O(n)
But we only store:
largest
number
A constant amount of extra memory:
Space → O(1)
So: O(n) time does NOT automatically mean O(n) space.
'''

# -----------------------Questions-------------
'''
Question 1
What are the time and space complexities?
def example(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
Answer:
Time = ?
Space = ?
And explain why.

Question 2
def example(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result
Answer:
Time = ?
Space = ?
'''
'''

Answers: q1 ,answer is -> the Time is linear O(n) beacause loop has to iterate over every element to add to total ,
 and the Space is constant O(1) cuz total isn't taking any other extra memory because it is taken and is updating ,
   by the exist list values of numbers.  

q2 , answer is -> Time is linear O(n) cuz of iteration for all elements in numbers ,
 Space is also linear O(n) cuz of result is holding new value each time it iterates ,
 so result is not updating but it holds older data like the value of first iteration and then all upto the last .
'''


# --------------Space Complexity Completed-----------------
