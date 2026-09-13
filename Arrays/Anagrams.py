# ------------Anarams---------------

'''
Two strings are anagrams if they contain the same characters with the same frequencies, just potentially in a different order.

Example:

"listen"
"silent"

Both contain:

l → 1
i → 1
s → 1
t → 1
e → 1
n → 1

So they are anagrams.
'''

'''
😂 I see what happened. Your frequency counting part is correct, but the condition is wrong:

if char != frequency[char]:

You're comparing a character ('h') with a number (1), so 'h' != 1 is immediately True and your loop breaks on the first character.

Correct logic

You need to:

1. Build the complete frequency dictionary first.

text = "hello"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

Now:

{'h': 1, 'e': 1, 'l': 2, 'o': 1}

2. Traverse the string again and find the first character whose frequency is 1:

for char in text:
    if frequency[char] == 1:
        print(char)
        break

Output:

h
Why two loops?

Because "first" and "frequency" are two different pieces of information.

First loop:

"How many times does every character occur?"

Second loop:

"Which character with frequency 1 appears first?"

Both loops are O(n), so:

O(n) + O(n) = O(n) ✅

This is a very important DSA pattern: build information first, then use it to answer the question.

Your frequency dictionary itself was 100% correct. We just needed to separate the two operations.

text = "hello"

frequency = {}

for char in text :

    if char in frequency:

        frequency[char] += 1

    else:

        frequency[char] = 1

for char in text:

    if frequency[char] == 1:

        print(char)

        break 

🔥 Exactly! Now it's 100% correct.

Your two-pass approach is the right DSA solution:

for char in text:
    # build frequency

then:

for char in text:
    if frequency[char] == 1:
        print(char)
        break

Output:

h
Complexity
Time: O(n) + O(n) = O(n) ✅
Space: O(k) ✅
Pattern: Frequency Map + Second Pass 🔥

This pattern is worth remembering because it appears constantly in interview problems.

✅ Character Frequency — DONE

Next, following your roadmap exactly:

👉 
Anagrams

next
Anagrams 🔥

Next exact topic in your roadmap.

Two strings are anagrams if they contain the same characters with the same frequencies, just potentially in a different order.

Example:

"listen"
"silent"

Both contain:

l → 1
i → 1
s → 1
t → 1
e → 1
n → 1

So they are anagrams.

The DSA connection

You just learned Character Frequency.

That's exactly what we're going to use here:

If two strings have identical character-frequency maps, they are anagrams.

For example:

"hello"
"olleh"

Frequency of both:

h → 1
e → 1
l → 2
o → 1

Therefore → anagrams ✅

Complexity

If the strings have length n:

Time: O(n)
Space: O(k), where k = distinct characters
'''

'''
Your challenge 🧠

Write a function:

def is_anagram(text1, text2):
    ...

Test it with:

text1 = "listen"
text2 = "silent"

Expected:

True

Then test:

text1 = "hello"
text2 = "world"

Expected:

False
Rules
Use a frequency dictionary
❌ Don't use sorted()
❌ Don't use any anagram library/function
✅ O(n) average time
'''

# text1 = "listen"
# text2 = "silent"

# frequency1 = {}

# for char in text1:
#     if char in frequency1:
#         frequency1[char] += 1
#     else:
#         frequency1[char] = 1 

# frequency2 = {}

# for char in text2:
#     if char in frequency2:
#         frequency2[char] += 1
#     else:
#         frequency2[char] = 1 


# if frequency1 == frequency2:
#     print(True)
# else:
#     print(False)

'''
Complexity
Time: O(n + m) → O(n) if both strings are roughly the same length
Space: O(k) for the frequency dictionaries
Pattern: Frequency Map → Compare Maps ✅

One small optimization: you can immediately return False if the strings have different lengths, because different-length strings can't be anagrams.
'''

'''
def is_anagram(text1, text2):
    if len(text1) != len(text2):
        return False

    frequency = {}

    for char in text1:
        frequency[char] = frequency.get(char, 0) + 1

    for char in text2:
        if char not in frequency:
            return False

        frequency[char] -= 1

        if frequency[char] == 0:
            del frequency[char]

    return len(frequency) == 0


print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))

Output:

True
False
'''  

'''
Uses one dictionary instead of two
Checks unequal lengths immediately
Counts the first string
Uses the second string to cancel those counts
Returns as soon as it detects something impossible
Still runs in O(n) average time
Uses O(k) space

The important pattern is:

String 1 → add frequencies
String 2 → subtract frequencies
Everything cancels → Anagram
'''

# ------------Anagrams Completed------------
