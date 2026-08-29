'''
That $O(1)$ and $O(n)$ notation is not complex higher-level math—it is just Big-O Notation,
 a simple shorthand way software developers measure two things:Time: How much slower code runs as data grows.
 Space: How much extra RAM/memory code consumes.
 Big-O ignores exact seconds because a fast processor runs code quicker than a slow one.
 Instead, it counts how many basic steps your computer performs relative to n (the number of items in your input list).
 The Big-O Reference
|Guide                                  | Notation           | Name        |
|                                       |--------------------|             |
|What it actually meansPractical Analogy| O(1)Constant       | TimeInstant.| Takes the same number of steps whether
                                        |                    |             |  you have 5 items or 5,000,000 items.

Looking up a page number directly 
from a book's index.                     O(n)Linear           TimeProportional. If items double (n x 2), steps double.
Reading a book page by page from start to finish.$O(n^2)$Quadratic TimeSlow. Nested loops. If items double ($n \times 2$), steps quadruple ($n \times 4$).Comparing every student in a classroom with every other student.$O(\log n)$Logarithmic TimeFast. Cuts problem size in half every step.Looking up a word in a paper dictionary by opening to the middle.Step-by-Step Code ExamplesExample 1: Constant Time — $O(1)$This function only takes 1 step, regardless of list size.Pythondef get_first_item(items: list) -> int:
    return items[0]  # Instant lookup by index -> O(1) Time
Example 2: Linear Time — $O(n)$If items has 10 elements, the loop runs 10 times. If it has 1,000 elements, it runs 1,000 times.Pythondef print_all_items(items: list) -> None:
    for item in items:  # Runs 'n' times -> O(n) Time
        print(item)
Example 3: Quadratic Time — $O(n^2)$A loop inside a loop. If items has 10 elements, the inner code runs $10 \times 10 = 100$ times.Pythondef print_pairs(items: list) -> None:
    for i in items:
        for j in items:  # n x n operations -> O(n^2) Time
            print(i, j)
Why Big-O Matters for InterviewsWhen companies like Google test your code, they do not just test if it works—they run it against huge datasets (e.g., $1,000,000$ items):An $O(n^2)$ algorithm will take ~11.5 days to run on 1,000,000 items.An $O(n)$ algorithm will take ~0.001 seconds on 1,000,000 items.The Two-Pointer approach discussed earlier runs in $O(n)$ linear time instead of $O(n^2)$ quadratic time because it avoids using nested loops.
'''   



