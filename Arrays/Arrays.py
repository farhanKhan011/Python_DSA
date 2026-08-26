# --------------DSA Arrays------------

'''
An array is a data structure used to store multiple elements .
Arrays are used by many algorithms.
For example, an algorithm can be used to look through an array to find the lowest value

'''
# In Python, an array can be created like this:
# my_array = [1,24,36,43,54,16]
# Note: The Python code above actually generates a Python 'list' data type, 
# but for the scope of this tutorial the 'list' data type can be used in the same way as an array

'''
Arrays are indexed, meaning that each element in the array has an index, a number that says where in the array the element is located. The programming language in this tutorial Python use zero-based indexing for arrays, meaning that the first element in an array can be accessed at index 0.

In Python, this code use index 0 to write the first array element (value 7) to the console:
'''
# my_array = [7,13,12,34,35]
# print(my_array[0])

'''
Algorithm: Find The Lowest Value in an Array
Let's create our first algorithm using the array data structure.
Below is the algorithm to find the lowest number in an array.
How it works:
Go through the values in the array one by one.
Check if the current value is the lowest so far, and if it is, store it.
After looking at all the values, the stored value will be the lowest of all values in the array.
'''
'''
Implementation
Before implementing the algorithm using an actual programming language, it is usually smart to first write the algorithm as a step-by-step procedure.

If you can write down the algorithm in something between human language and programming language, the algorithm will be easier to implement later because we avoid drowning in all the details of the programming language syntax.

Create a variable 'minVal' and set it equal to the first value of the array.
Go through every element in the array.
If the current element has a lower value than 'minVal', update 'minVal' to this value.
After looking at all the elements in the array, the 'minVal' variable now contains the lowest value.
You can also write the algorithm in a way that looks more like a programming language if you want to, like this:
'''
'''
variable 'minVal' = array[0]
For each element in the array 
    if current element < minVal:
        minVal = current element
'''
'''
Note: The two step-by-step descriptions of the algorithm we have written above can be called 'pseudocode'. 
Pseudocode is a description of what a program does, using language that is something between human language 
and a programming language.
'''
# After we have written down the algorithm, it is much easier to implement the algorithm in a specific programming language:





