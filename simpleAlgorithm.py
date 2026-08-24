# ---------A Simple Algorithm-------
# Fibonacci Numbers
'''The Fibonacci numbers are very useful for introducing algorithms, so before we continue,
 here is a short introduction to Fibonacci numbers.
The Fibonacci numbers are named after a 13th century Italian mathematician known as Fibonacci.
The two first Fibonacci numbers are 0 and 1, and the next Fibonacci number is always the sum of the two previous numbers, 
so we get 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
'''
'''
 let's implement three different versions of the algorithm to create Fibonacci numbers, just to see the difference between programming with loops and programming with recursion in a simple way.
'''
'''
The Fibonacci Number Algorithm
To generate a Fibonacci number, all we need to do is to add the two previous Fibonacci numbers.
The Fibonacci numbers is a good way of demonstrating what an algorithm is. We know the principle of how to find the next number, so we can write an algorithm to create as many Fibonacci numbers as possible.
Below is the algorithm to create the 20 first Fibonacci numbers.
'''
# How it works:
'''
Start with the two first Fibonacci numbers 0 and 1.
Add the two previous numbers together to create a new Fibonacci number.
Update the value of the two previous numbers.
Do point a and b above 18 times.
'''
'''
Loops vs Recursion
To show the difference between loops and recursion, we will implement solutions to find Fibonacci numbers in three different ways:

An implementation of the Fibonacci algorithm above using a for loop.
An implementation of the Fibonacci algorithm above using recursion.
Finding the 
n
th Fibonacci number using recursion.
'''
'''
1. Implementation Using a For Loop
It can be a good idea to list what the code must contain or do before programming it:

Two variables to hold the previous two Fibonacci numbers
A for loop that runs 18 times
Create new Fibonacci numbers by adding the two previous ones
Print the new Fibonacci number
Update the variables that hold the previous two fibonacci numbers
Using the list above, it is easier to write the program:
'''
# b = 1
# a = 0
# for fabo in range(18):
#     newfebo = a + b
#     print(newfebo)
#     a = b
#     b = newfebo
'''
the output is :
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
'''
'''
2. Implementation Using Recursion
Recursion is when a function calls itself.
To implement the Fibonacci algorithm we need most of the same things as in the code example above,
 but we need to replace the for loop with recursion.
To replace the for loop with recursion, we need to encapsulate much of the code in a function, 
and we need the function to call itself to create 
a new Fibonacci number as long as the produced number of Fibonacci numbers is below, or equal to, 19.
Our code looks like this:
'''
# print(0)
# print(1)
# count = 2 

# def fabonacci(a , b):
#     global count 
#     if count <=19:
#         newfabo = a + b 
#         print(newfabo)
#         a = b 
#         b = newfabo
#         count += 1
#         fabonacci(a , b )
#     else:
#         return
# fabonacci(0,1)
'''
output : 0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
'''

'''
Finding The nth Fibonacci Number Using Recursion
To find the nth Fibonacci number we can write code based on the mathematic formula for Fibonacci number n:
          F(n) = F(n - 1) + F(n - 2)
This just means that for example the 10th Fibonacci number is the sum of the 9th and 8th Fibonacci numbers.
Note: This formula uses a 0-based index. This means that to generate the 20th Fibonacci number, we must write F(19).
When using this concept with recursion, we can let the function call itself as long as 
n is less than, or equal to, 1. If n≤1
 it means that the code execution has reached one of the first two Fibonacci numbers 1 or 0.
'''
# The code looks like this:
# def F(n):
#     if n <= 1:
#         return n 
#     else:
#         return F(n - 1) + F(n - 2)
# print(F(19))

'''
now let me explain this small block of code well i teach it to my self on a page so here I will show you that in this note 
lets instead of 19 we are passing the 3 , like what is the 3rd in fabonacci , like assume that it is nth so the code find it like this 
def F(3):
    if 3 <= 1:
        return 3 
    else:
        return F(2) + F(1) # cuz 3 - 1 = 2 and 3-2 = 1
        now after this since its recursion so the F(2) and F(1) means the function invoke itself twice so again
        lets F2 calls it self like this def F(2):                 | and F1 calls itself like this  
                                            if 2 <= 1 :           |    def F(1):                         
                                                return 2          |         if 1 <= 1:
                                            else:                 |             return 1
                                                return F(1) + F(0)|     else:
                                                                  |         return F(0) + F(-1) 
              here in the same process it will return at the end 1|   so here the function will finally return 1 
    so finaly to add that two 1s like 1 + 1 which is 2 so that is the final answer which means that in fabonacci ,
    the 3rd number will be 2 , and it is like 0 , 1 , 1 , 2 , 3 here many of thinks the 3rd is 1 but since here the index is
start with 0 so which means on index 3 the value is 2 . and if you do the same for that 19 so the nth term or value will be 4181

There are two important things to notice here: The amount of function calls, 
and the amount of times the function is called with the same arguments.
So even though the code is fascinating and shows how recursion work,
 the actual code execution is too slow and ineffective to use for creating large Fibonacci numbers.
'''
'''
Summary:
Before we continue, let's look at what we have seen so far:
An algorithm can be implemented in different ways and in different programming languages.
Recursion and loops are two different programming techniques that can be used to implement algorithms.
'''
# --------Simple Algorithm Completed---------