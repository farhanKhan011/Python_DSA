# --------------------Big-Θ (Big-Theta)-----------------

'''
What is Big-Θ?

Big-Θ describes the tight bound of an algorithm.

In simple terms:

Big-O → upper bound
Big-Ω → lower bound
Big-Θ → tight bound

When an algorithm's growth is both bounded above and below by the same function, we use Θ.
'''

'''
Simple Example
def example(numbers):
    for number in numbers:
        print(number)

There are n elements.

The loop always processes all n elements.

Therefore:

O(n)  → upper bound
Ω(n)  → lower bound
Θ(n)  → tight bound

So we can say:

Time Complexity = Θ(n)

3. Why Is Θ Called "Tight"?

Imagine the algorithm's actual growth is approximately proportional to n.

It isn't merely at most n, and it isn't merely at least n.

It's actually growing at the same rate as n.

So:

Ω(n)  ≤ actual growth ≤  O(n)

          ↓
       Θ(n)

That's the idea of a tight bound.
'''

'''
Linear Search Example

Remember our search:

def search(numbers, target):
    for number in numbers:
        if number == target:
            return True

    return False

If the target is the first element:

Ω(1)

If the target is last or doesn't exist:

O(n)

Can we say the algorithm is always Θ(n)?

No. ❌

Because the amount of work depends on where the target is.

Its best case and worst case are different.
'''

'''
Compare With This
def example(numbers):
    total = 0

    for number in numbers:
        total += number

    return total

This always visits every element.

Therefore:

Ω(n)
O(n)
Θ(n)

All three describe the same asymptotic growth.

'''
# 🔥 The Three Together
'''
Question 1

What is the Θ complexity?

def example(numbers):
    for number in numbers:
        print(number)
Question 2

What about this?

def example(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
'''
# for the first one loop has to iterate for every single element  , so its Θ(n)  , and for Q2:  n x n = n^2 -> Θ   (n^2) 

# -----------Bit-Theta Completed-------------------
