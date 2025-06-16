"""
Key Differences:
- Lists: Built-in, dynamic, heterogeneous (any data type)
- Arrays (from `array` module): Homogeneous (fixed type), memory-efficient
"""

import array  # For native arrays
import numpy as np  # For NumPy arrays (optional but common in practice)

# --------------------------
# 1. Python Lists (Dynamic Arrays)
# --------------------------
py_list = [1, 2, "three", True]  # Heterogeneous, O(1) append
py_list.append(4.5)  # [1, 2, 'three', True, 4.5]

# Memory Overhead (Lists store extra metadata)
print(f"List size: {py_list.__sizeof__()} bytes")  # ~104 bytes (varies)

# --------------------------
# 2. Native Arrays (Fixed-Type)
# --------------------------
# 'i' = signed integer, 'd' = double (float)
int_array = array.array('i', [1, 2, 3, 4])  # Homogeneous, compact
int_array.append(5)  # O(1) amortized
try:
    int_array.append("text")  # TypeError: integer argument expected
except TypeError as e:
    print(f"Array type constraint: {e}")

# Memory Efficiency
print(f"Array size: {int_array.__sizeof__()} bytes")  # ~68 bytes

# --------------------------
# 3. NumPy Arrays (Scientific Computing)
# --------------------------
np_array = np.array([1.5, 2.5, 3.5], dtype=np.float32)  # Homogeneous, vectorized ops
print(np_array * 2)  # [3., 5., 7.] (O(1) time, no loops)

# Memory Comparison
print(f"NumPy array size: {np_array.nbytes} bytes")  # 12 bytes (4 bytes per float32)

# --------------------------
# 4. When to Use Each
# --------------------------
"""
| Feature          | List          | Array (`array`) | NumPy Array |
|------------------|---------------|-----------------|-------------|
| Data Types       | Any           | Fixed           | Fixed       |
| Memory Use       | High          | Medium          | Low         |
| Speed            | Moderate      | Fast            | Very Fast   |
| Use Case         | General-purpose | Low-level C-like | Math/ML    |
"""

# --------------------------
# 5. Performance Benchmark
# --------------------------
from timeit import timeit

# Summing 1M elements
list_time = timeit('sum(lst)', setup='lst=list(range(1_000_000))', number=100)
array_time = timeit('sum(arr)', setup='import array; arr=array.array("i", range(1_000_000))', number=100)
numpy_time = timeit('np.sum(np_arr)', setup='import numpy as np; np_arr=np.arange(1_000_000)', number=100)

print(f"List: {list_time:.4f}s\nArray: {array_time:.4f}s\nNumPy: {numpy_time:.4f}s")
# Typical Output:
# List: 1.2345s
# Array: 0.8765s
# NumPy: 0.0123s

# --------------------------
# 6. Practical Applications
# --------------------------
# Lists: JSON data, general sequences
user_data = ["Alice", 30, True, ["Python", "SQL"]]

# Arrays: Binary I/O, memory-sensitive tasks
with open('data.bin', 'wb') as f:
    int_array.tofile(f)  # Compact binary storage

# NumPy: Numerical computations
matrix = np.random.rand(1000, 1000)  # 1M elements, efficient linear algebra

# --------------------------
# 7. Exercises
# --------------------------
# 1. Convert list to array and benchmark
def list_to_array(lst):
    return array.array('i', lst)  # O(n) time

# 2. Find memory savings using arrays
def memory_savings(lst):
    list_size = lst.__sizeof__()
    arr_size = array.array('i', lst).__sizeof__()
    return list_size - arr_size

print(f"Memory saved: {memory_savings(list(range(100)))} bytes")