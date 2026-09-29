# -------------Radix Sort-----------

'''
Radix Sort is another non-comparison sorting algorithm.

The key idea:

Instead of comparing entire numbers, sort numbers digit by digit.

For example:

[170, 45, 75, 90, 802, 24, 2, 66]

We process:

Ones digit
Tens digit
Hundreds digit

And importantly, each digit pass uses a stable Counting Sort.
'''

'''
1. Why stability matters

Take:

[170, 45, 75, 90]

Sort by the ones digit:

170 → 0
90  → 0
45  → 5
75  → 5

Because the sorting is stable:

[170, 90, 45, 75]

Notice 170 remains before 90, and 45 remains before 75.

Then we sort that result by the tens digit.

That's why we specifically learned stable Counting Sort before Radix Sort.

'''

'''
LSD Radix Sort

The version you'll most commonly implement is LSD (Least Significant Digit) Radix Sort.

Start with the rightmost digit:

ones → tens → hundreds → thousands → ...

For:

[170, 45, 75, 90, 802, 24, 2, 66]

Conceptually:

Original
[170, 45, 75, 90, 802, 24, 2, 66]

ones digit
        ↓
[170, 90, 802, 2, 24, 45, 75, 66]

tens digit
        ↓
[802, 2, 24, 45, 66, 170, 75, 90]

hundreds digit
        ↓
[2, 24, 45, 66, 75, 90, 170, 802]

Now it's sorted.
'''

'''
Implementation
We can use Counting Sort specifically for one digit.
'''
def counting_sort_digit(nums, exp):
    n = len(nums)
    output = [0] * n
    count = [0] * 10

    # Count digits
    for num in nums:
        digit = (num // exp) % 10
        count[digit] += 1

    # Cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Stable placement
    for i in range(n - 1, -1, -1):
        digit = (nums[i] // exp) % 10

        count[digit] -= 1
        output[count[digit]] = nums[i]

    # Copy back
    for i in range(n):
        nums[i] = output[i]


def radix_sort(nums):
    if not nums:
        return

    max_value = max(nums)

    exp = 1

    while max_value // exp > 0:
        counting_sort_digit(nums, exp)
        exp *= 10 


nums = [170, 45, 75, 90, 802, 24, 2, 66]

radix_sort(nums)

print(nums)

