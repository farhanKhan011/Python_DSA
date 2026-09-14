# ------------Linear Search----------


'''
What is Linear Search?

Linear Search means checking elements one by one from left to right until we find what we're looking for.

Example:

numbers = [4, 8, 2, 9, 5]
target = 9

4 ❌
8 ❌
2 ❌
9 ✅
Python
def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

    return -1

Usage:

print(linear_search([4, 8, 2, 9, 5], 9))

Output:

3

Because 9 is at index 3.

🧠 The pattern
for each element:
    check if it is the target
        ↓
    found → return index
        ↓
    not found → continue
'''

'''
Complexity

Best case: O(1) — target is first.

Worst case: O(n) — target is last or doesn't exist.

Space: O(1)
'''

'''
🎯 Your turn

Write linear_search() yourself.

Test it with:

numbers = [10, 4, 7, 2, 15, 8]

print(linear_search(numbers, 15))  # 4
print(linear_search(numbers, 99))  # -1
'''

# def linear_search(numbers , target):
#     for i in range(len(numbers)):
#         if numbers[i] == target:
            
#             return i
#     return -1 

#             OR

def linear_search(numbers, target):
    for i, number in enumerate(numbers):
        if number == target:
            return i
    return -1

numbers = [10, 4, 7, 2, 15, 8]

print(linear_search(numbers , 15))
print(linear_search(numbers , 99))

'''
Both are O(n) time, O(1) space.

For DSA, I'd use the enumerate() version. ✅
'''

# ---------------Linear Search Completed-----------------
