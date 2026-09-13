# -------------String Manipulation--------------

'''
String Manipulation 🔥

Next exact topic in your roadmap.

Strings are sequences of characters:

text = "Google"

You can access characters by index:

text[0]   # G
text[3]   # g

Like arrays, traversal is usually:

for char in text:
    print(char)
Important DSA idea

In string problems, you'll frequently need to:

Traverse characters
Compare characters
Build/modify strings
Track positions
Check conditions
Work with substrings

For example, manually count the length:

text = "Google"

count = 0

for char in text:
    count += 1

print(count)

Output:

6

That's O(n) time.
'''

'''
Your first challenge 🧠

Given:

text = "Google"

Create a new string containing the characters in reverse order.

Expected:

"elgooG"

Rules:

❌ Don't use [::-1]
❌ Don't use reversed()
❌ Don't use .reverse()
✅ Traverse the string yourself
'''

# text = "Google"
# a = len(text) - 1 
# result = ''

# for _ in range(len(text)):
#     result += text[a]
#     a -= 1
# print(result)

'''
Complexity:

Time: O(n)
Space: O(n)
'''

'''
Compare Characters

Given:

text = "hello"

We want to determine whether the first and last characters are equal.

Expected:

False
'''
# text = 'hello'

# first = text[0]
# last = text[-1]
# if first == last :
#     print(True)
# else:
#     print(False)
    
'''
Build/Modify Strings
text = "hello world"

Create a new string containing only the characters that are not spaces.

Expected:

"helloworld"

Use a loop and a result string. No .replace().
'''
# text = "hello world"
# newText = ''

# for char in text:
#     if char != ' ':
#         newText += char
# print(newText)
    
'''
text = "programming"

Find the index of the first occurrence of "g" using a loop.

Expected:

3

Rules:

❌ Don't use .find()
❌ Don't use .index()
✅ Use a loop
✅ Track the position yourself
'''
text = "programming"
# counter = 0 
# for i , char in enumerate(text):
#     if char == 'g':
#         counter = i 
#         break
# print(counter)

# for i , char in enumerate(text):
#     if char == 'g':
#         print(i)
#         break

'''
Substring

A substring is a contiguous sequence of characters inside a string.

"programming"
   └────┘
  "gram"

For example:

text = "programming"

print(text[3:7])

Output:

gram

The important DSA idea is understanding where a substring starts and ends.
'''

    # --------String Maniputlate Completed----------------