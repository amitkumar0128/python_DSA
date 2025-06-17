"""
Strings: Immutable sequences of Unicode characters
Key Concepts: Immutability, Slicing, Common Algorithms
"""

# --------------------------
# 1. Core Properties
# --------------------------
s = "Hello, World!"

# Immutability
try:
    s[0] = 'h'
except TypeError:
    print("Strigs are immutable! Create new strings instead.")

# Length and Memory
print(f"Length: {len(s)}") # 13
print(f"Memory Size: {s.__sizeof__()} bytes") # 62 bytes (overhead + content)

# --------------------------
# 3. Common Methods
# --------------------------
# Case Conversion (O(n))
print("hello".upper())  # 'HELLO'

# Searching (O(n))
print("Hello, World!".find("World"))  # 7
print("world" in "Hello, World!")  # True

# Splitting (O(n))
parts = "apple, banana, cherry".split(", ") # ['apple', 'banana', 'cherry']
print(parts)

# --------------------------
# 4. Key Algorithms
# --------------------------
# Palindrome Check (O(n))
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # True

# String Compression O(n)
def compress(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(f"{s[i-1]}{count}")
            count = 1
    compressed.append(f"{s[-1]}{count}")
    return min(s, ''.join(compressed), key=len)

print(compress("aabcccccaaa"))  # 'a2b1c5a3'

# --------------------------
# 5. Performance Tips
# --------------------------
# Anti-Pattern: Slow concatenation (O(n²))
result = ""
for c in ["a", "b", "c", "d", "e"]:
    result += c # Bad: New string created each time

# Optimized: str.join() (O(n))
result  =  "".join(["a", "b", "c", "d", "e"])  # Good: Single allocation

# --------------------------
# 6. Exercises
# --------------------------
# 1. Custom string replacement
def custom_replace(s, old, new):
    return new.join(s.split(old))

# 2. Longest unique substring (O(n))
def longest_unique_substring(s):
    used = {}
    start = max_len = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_len = max(max_len, i - start + 1)
        used[c] = i
    return max_len

print(longest_unique_substring("abcabcbb"))  # 3 ('abc')

# 3. Anagram check (O(n))
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))  # True

# 4. Regex Validator (O(n))
import re
def is_valid_email(email):
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email))

print(is_valid_email("test@example.com"))  # True