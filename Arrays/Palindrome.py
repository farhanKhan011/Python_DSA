# -----------Palindrome--------------

'''
A palindrome is something that reads the same forward and backward.

Examples:

racecar → racecar ✅
level   → level   ✅
madam   → madam   ✅
hello   → olleh   ❌
🧠 Best DSA pattern: Two Pointers

We don't need to reverse the entire string.

Use two pointers:

r a c e c a r
↑           ↑
L           R

Compare:

s[L] == s[R]

Then move inward:

  r a c e c a r
    ↑       ↑

Continue until the pointers meet.

Python — clean interview version
'''
# def is_palindrome(text):
#     left = 0
#     right = len(text) - 1

#     while left < right:
#         if text[left] != text[right]:
#             return False

#         left += 1
#         right -= 1

#     return True

'''
Complexity
Time: O(n)
Space: O(1)

This is the preferred DSA solution because we're checking the string in place without creating a reversed copy.
'''

'''
🎯 Your turn

Write the function yourself and test:

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("level"))    # True
'''
def is_palindrome(text):
    left = 0 
    right = len(text) - 1 

    while left < right :
        if text[left] != text[right]:
            return False

        left += 1 
        right -= 1

    return True 

print(is_palindrome("racecar"))  
print(is_palindrome("hello"))    
print(is_palindrome("level"))    


# ----------------palindrome Completed---------------