"""
Big-O Cheat Sheet:
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
"""

# --------------------------
# 1. Constant Time: O(1)
# --------------------------
def get_first_element(lst):
    return lst[0]  # Single operation, independent of input size

# Use Case: Accessing dictionary values or array indices
print(get_first_element([10, 20, 30]))  # Output: 10

# --------------------------
# 2. Linear Time: O(n)
# --------------------------
def linear_search(lst, target):
    for item in lst:  # Grows linearly with input
        if item == target:
            return True
    return False

# Use Case: Unsorted list search
print(linear_search([5, 2, 9, 1], 9))  # Output: True

# --------------------------
# 3. Quadratic Time: O(n²)
# --------------------------
def find_pairs(lst):
    pairs = []
    for i in lst:          # Nested loop
        for j in lst:
            pairs.append((i, j))
    return pairs

# Use Case: Comparing all pairs (e.g., matrix operations)
print(find_pairs([1, 2]))  # Output: [(1,1), (1,2), (2,1), (2,2)]

# --------------------------
# 4. Logarithmic Time: O(log n)
# --------------------------
def binary_search(sorted_lst, target):
    low, high = 0, len(sorted_lst)-1
    while low <= high:
        mid = (low + high) // 2
        if sorted_lst[mid] == target:
            return mid
        elif sorted_lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Use Case: Searching in sorted data (optimal for large datasets)
print(binary_search([1, 3, 5, 7, 9], 5))  # Output: 2

# --------------------------
# 5. Space Complexity
# --------------------------
def duplicate_list(lst):
    return lst + lst  # O(n) space (creates new list)

def constant_space_sum(n):
    total = 0          # O(1) space (single variable)
    for i in range(n):
        total += i
    return total

# --------------------------
# 6. Practical Constraints
# --------------------------
"""
    1 second = 10^8 operations

| Input Size (n) | Feasible Complexity  |
|----------------|----------------------|
| n > 10^8       | O(log n)       O(1)  |
| n ≤ 10^8       | O(n)                 |
| n ≤ 10^6       | O(n log n)           |
| n ≤ 10^4       | O(n²)                |
| n ≤ 500        | O(n³)                |
| n ≤ 20         | O(2ⁿ) or O(n!)       |
"""

# --------------------------
# 7. Recursion Analysis
# --------------------------
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)  # O(n) time & space (call stack)

print(factorial(5))  # Output: 120

# --------------------------
# 8.  Python Data Structure Complexities
# --------------------------
"""
Operation Complexity Table:

  |  Operation	        |  List	|  Dict	|  Set	|  String |
  |---------------------|-------|-------|-------|---------|
  |  Index Access	    |  O(1)	|  N/A	|  N/A	|   O(1)  |
  |  Append/Add	        |  O(1)*|  O(1)*|  O(1)*|   N/A   |
  |  Search	            |  O(n)	|  O(1)	|  O(1)	|   O(n)  |
  |  Insert/Delete Mid	|  O(n)	|  O(1)	|  O(1)	|   O(n)  |
"""

# timeit usage
import timeit
setup = "lst = list(range(10000))"
stmt = "sum(lst)"  # O(n) operation
time = timeit.timeit(stmt, setup, number=1000)
print(f"Time: {time:.6f} seconds")

# List membership test: O(n)
list_time = timeit.timeit('999 in lst', 
                          setup='lst=list(range(1000))', 
                          number=10000)

# Dict membership test: O(1)
dict_time = timeit.timeit('999 in dct', 
                          setup='dct={i:1 for i in range(1000)}', 
                          number=10000)

print(f"List: {list_time:.4f}s | Dict: {dict_time:.4f}s")
# Typical output: List: 0.25s | Dict: 0.0007s