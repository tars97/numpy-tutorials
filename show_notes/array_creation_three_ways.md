
# NumPy Array Creation: 3 Ways in 4 Minutes

Numpy (*Num-Pie* or *Num-Pee* if you want to pronounce it the fun way) is a *ridiculously* useful Python library which allows for complex data processing at extremely high speeds (speeds which might be faster than if you wrote your own C-loops). It actually has an extremely elegant interface but it can be a bit scary since it might not look like code that you're used to. So let's start at the top and go over three ways to create a Numpy array in four minutes.

## \#1: Empty Arrays

This is probably the most general, catch-all way you'll want to create an array in Numpy. You just want a big buffer with enough space for however many numbers or pieces of data you want to put in. There are a few approaches to go over here. The most common is probably when you just want an array full of zeros that you can do whatever you want with later. For that, NumPy has a function called `zeros`.

```python
import numpy as np

zeros_array = np.zeros(100, dtype=np.int32)
zeros_md_array = np.zeros((10, 10), dtype=np.float64)

print('ZEROS:')
print('Single-dimensional:')
print(zeros_array)
print('Multi-dimensional:')
print(zeros_md_array)
```

<details>
    <summary>Output</summary>
    <pre>
    ZEROS:
    Single-dimensional:
    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    Multi-dimensional:
    [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
    </pre>
</details>
    

Simply provide the size of your desired array as the first argument, and provide your desired data type as a keyword argument under 'dtype'. For multi-dimensional arrays, make the size a tuple instead of an integer.

If you want the array filled with ones, that's equally easy. Same exact syntax, but call `ones` instead of `zeros`.



```python
ones_array = np.ones(50, dtype=np.bool)
ones_md_array = np.ones((10, 10), dtype=np.float32)

print('ONES:')
print('Single dimensional:')
print(ones_array)
print('Multi-dimensional:')
print(ones_md_array)
```
<details>
    <summary>Output</summary>
    <pre>
    ONES:
    Single dimensional:
    [ True  True  True  True  True  True  True  True  True  True  True  True
      True  True  True  True  True  True  True  True  True  True  True  True
      True  True  True  True  True  True  True  True  True  True  True  True
      True  True  True  True  True  True  True  True  True  True  True  True
      True  True]
    Multi-dimensional:
    [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]
    </pre>
</details>

Note that if you want an array of booleans, `zeros` will make an array of `false` values, and `ones` will make an array of `true` values.

The last type of empty array is for when you plan to overwrite every single value in an array, and thus don't care whether its values are initialized with ones, zeros, or any numbers at all. For that, just call `empty`. Again, same syntax as `zeros` and `ones`. Numpy is just going to ask your operating system for a section of memory and hand it back to you as an array. It will just contain whatever junk values happened to be in that particular section of memory at the time. This will be different run-over-run. So be cautious when using this method--make sure your program writes a value to every element before use, otherwise you'll end up with some very unexpected results. It may however be slightly faster than if numpy asks your operating system for a chunk of memory full of zeros, although this is mostly going to be insignificant.


```python
empty_array = np.empty(50, dtype=np.bool)
empty_md_array = np.empty((10, 10), dtype=np.float32)

print('EMPTY:')
print('Single-dimensional:')
print(empty_array)
print('Multi-dimensional:')
print(empty_md_array)
```
<details>
    <summary>Output</summary>
    <pre>
    EMPTY:
    Single-dimensional:
    [ True  True  True  True  True  True False False  True  True  True  True
      True  True False False  True  True  True  True  True  True False False
      True  True  True  True  True  True False False  True  True  True  True
      True  True False False  True  True  True  True  True  True False False
      True  True]
    Multi-dimensional:
    [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]
    </pre>
</details>

## \#2: Synthetic Arrays

When I say "synthetic arrays" I just mean arrays which contain some sort of generated sequence which you can use as a starting point for your computations. The most common is probably just an array which counts 0, 1, 2... up until the end of the array. These are often used as the axis for a graph or as an index array. To make such an array in Numpy, use the `arange` function.


```python
zero_to_ten = np.arange(10)
twenty_to_thirty = np.arange(20, 30)
ten_by_twos = np.arange(0, 10, 2)

print('ARANGE:')
print('One parameter:')
print(zero_to_ten)
print('Two parameters:')
print(twenty_to_thirty)
print('Three parameters:')
print(ten_by_twos)
```
<details>
    <summary>Output</summary>
    <pre>
    ARANGE:
    One parameter:
    [0 1 2 3 4 5 6 7 8 9]
    Two parameters:
    [20 21 22 23 24 25 26 27 28 29]
    Three parameters:
    [0 2 4 6 8]
    </pre>
</details>

If you just specify one parameter it will be assumed that you want an array which counts from zero up to that number. You can also specify a certain range of numbers by specifying the starting point as the first parameter and the stopping point as the second. Finally, you can also specify a "step" parameter if you want to count by twos, for example. There are plenty of other ways to create synthetic arrays in Numpy, but in the interest of time, let's move on.

## \#3: Data arrays

This last way is fairly self-explanitory. Say you have a large set of data collected from some kind of instrument or generated by scraping the web, for instance. There are lots of ways you could store this data but for the purposes of this video I'm going to assume you have it stored in a .csv file. If you have just one data type you can easily retrieve the data as a Numpy array using the function `loadtxt`. Simply provide a file name or path as the first parameter, and since .csv stands for "comma separated values", we'll specify that the data are separated by commas using the "delimiter" keyword argument. We can also specify a data type using the "dtype" keyword. Numpy will assume floats if you don't specify one. If your data has a header row, we'll need to tell numpy to skip it using the 'skiprows' parameter.

```
my_data.csv
===========
time,distance
0,0
1,10
2,100
3,1000
4,100
5,10
6,0
```


```python
my_data = np.loadtxt('my_data.csv', delimiter=',', dtype=np.int32, skiprows=1)
print(my_data)
```
<details>
    <summary>Output</summary>
    <pre>
    [[   0    0]
     [   1   10]
     [   2  100]
     [   3 1000]
     [   4  100]
     [   5   10]
     [   6    0]]
    </pre>
</details>

If your data set has multiple types, it's a tiny bit more complicated but still surprisingly simple. We'll need to specify the data type as a structured array. The easiest way to do this is by providing numpy's `dtype` function with a list of the different types in order along with custom names as tuples.

```
het_data.csv
============
time,distance,is_in_lead
0,0,0
1,6.9805,1
2,19.7802,1
3,25.8012,0
```


```python
column_types = np.dtype([('time', np.int32), ('distance', np.float32), ('is_in_lead', np.bool)])
heterogeneous_data = np.loadtxt('het_data.csv', delimiter=',', dtype=column_types, skiprows=1)
print(heterogeneous_data)
```
<details>
    <summary>Output</summary>
    <pre>
    [(0,  0.    , False) (1,  6.9805,  True) (2, 19.7802,  True)
     (3, 25.8012, False)]
    </pre>
</details>

We can then easily separate out the different columns from the data by indexing the result using the column names we provided.


```python
print(heterogeneous_data['time'])
```
<details>
    <summary>Output</summary>
    <pre>
    [0 1 2 3]
    </pre>
</details>

--which perfectly leads into my next Numpy video which will be all about indexing. See you then!
