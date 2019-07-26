import numpy as np

zeros_array = np.zeros(100, dtype=np.int32)
zeros_md_array = np.zeros((10, 10), dtype=np.float64)

print('ZEROS:')
print('Single-dimensional:')
print(zeros_array)

print('Multi-dimensional:')
print(zeros_md_array)

ones_array = np.ones(50, dtype=np.bool)
ones_md_array = np.ones((10, 10), dtype=np.float32)

print('ONES:')
print('Single-dimensional')
print(ones_array)

print('Multi-dimensional')
print(ones_md_array)

empty_array = np.empty(50, dtype=np.bool)
empty_md_array = np.empty((10, 10), dtype=np.float32)

print('EMPTY:')
print('Single-dimensional:')
print(empty_array)
print('Multi-dimensional:')
print(empty_md_array)




