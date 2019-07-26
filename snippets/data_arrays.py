import numpy as np

my_data = np.loadtxt('my_data.csv', delimiter=',', dtype=np.int32, skiprows=1)

print('my_data.csv:')
print(my_data)

column_types = np.dtype(
    [
        ('time', np.int32),
        ('distance', np.float32),
        ('is_in_lead', np.bool)
    ]
)

heterogeneous_data = np.loadtxt('het_data.csv', delimiter=',', dtype=column_types, skiprows=1)

print('het_data.csv:')
print(heterogeneous_data)

print('Time column:')
print(heterogeneous_data['time'])
