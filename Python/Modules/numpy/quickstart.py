#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def print_header(header):
    width = int((80-len(header))//2)
    print()
    print('~'*width, header, '~'*width)

def print_command(command, variables):
    # Access locals
    locals().update(variables)

    print('>> ' + str(command))
    try:
        result = str(eval(command))
        if result not in ['None', '']:
            print(result)
            print()
    except Exception:
        pass



def main():
    '''
    print_header('The Basics')

    print('# Generate array from range and change shape to matrix')
    a = np.arange(20).reshape(4, 5)

    print('# Number of axes (dimensions) of the array')
    print_command('a.ndim', locals())

    print('# Dimensions of the array indicating the size of the array in each dimension')
    print_command('a.shape', locals())

    print('# Total number of elements of the array = product of shape')
    print_command('a.size', locals())

    print('# Object describing data type of elements in the array')
    print_command('a.dtype', locals())

    print('# Size in bytes of each element of the array = ndarray.dtype.itemsize')
    print_command('a.itemsize', locals())

    print('# Buffer containing elements of the array. No need to use it')
    print_command('a.data', locals())

    breakpoint()

    print_header('Array Creation')

    print('# Create ndarray manually')

    print_command('b = np.array([2,3,4])', locals())
    print_command('b', locals())

    print('# Manual multidimensional array')
    b = np.array([(9, 2, 67), (8, 0, 35)])
    print_command('b = np.array([[9, 2, 67],  [8, 0, 35]])', locals())
    print_command('b', locals())

    print('# Assign type as array is being created')
    b = np.array([[1, 2], [2,4]], dtype=complex)
    print_command('b = np.array([[1, 2], [2,4]], dtype=complex)', locals())
    print_command('b', locals())

    breakpoint()

    print_header('Arrays with placeholder content')
    print_command('np.full((9,2), 1.5)', locals())
    print_command('np.ones((5, 2, 3), dtype=np.int16)', locals())
    print_command('np.zeros((3, 4))', locals())
    print_command('np.empty((2, 3))', locals())

    breakpoint()

    print_header('Automatically generated arrays')

    print('# From 10 to 30 in intervals of 5')
    print_command('np.arange(10, 30, 5)', locals())

    print('# From 0 to 10 in intervals of 1.5')
    print_command('np.arange(0, 10, 1.5)', locals())

    print('# 100 elements from 0 to 1 inclusive')
    print_command('np.linspace(0, 1, 12)', locals())
    print('# linspace\'s advantage is that its length is predictable')

    breakpoint()

    print_header('Fill already created arrays')

    b = np.linspace(1, 7, 10).reshape(2,5)
    print_command('b = np.linspace(1, 7, 10).reshape(2,5)', locals())

    print('# Fill array with specific number')
    print_command('np.full_like(b, 10, dtype=np.int32)', locals())

    print('# Fill array with ones')
    print_command('np.ones_like(b)', locals())

    print('# Fill array with zeros')
    print_command('np.zeros_like(b)', locals())

    print('# Empty array. Initialized array will probably have random numbers')
    print_command('np.empty_like(b)', locals())

    breakpoint()

    print_header('Baisc Operations')
    A = np.array([[0, 1], [2, 3]])
    print_command('A = np.array([[0, 1], [2, 3]])', locals())
    B = np.array([[4, 5], [6, 7]])
    print_command('B = np.array([[4, 5], [6, 7]])', locals())
    R = np.linspace(0, 2*np.pi, 17)
    print_command('R = np.linspace(0, 2*np.pi, 17)', locals())

    print('# All operations are done elementwise')
    print_command('A - B', locals())
    print_command('A ** 2', locals())
    print_command('B <= 6', locals())
    print_command('10 * np.sin(R)', locals())
    print_command('A * B', locals())

    print('# Matrix Product')
    print_command('A @ B', locals())
    print_command('A.dot(B)', locals())

    breakpoint()

    print_header('Upcasting')

    print('# When operating with arrays of different types, the type of the resulting')
    print('# array corresponds to the more general or precise one')

    A = np.ones((17), dtype=np.int32)
    print_command('A = np.ones((17), dtype=np.int32)', locals())
    R = np.linspace(0, 2*np.pi, 17)
    print_command('R = np.linspace(0, 2*np.pi, 17)', locals())
    print_command('A.dtype', locals())
    print_command('R.dtype', locals())

    C = R + A
    print_command('C = R + A', locals())
    print_command('C.dtype', locals())

    breakpoint()

    print_header('Unary operations')

    A = np.linspace(0, 10, 48).reshape(8, 6)
    print_command('A = np.linspace(0, 10, 48).reshape(8, 6)', locals())
    R = np.linspace(0, 2*np.pi, 17)
    print_command('R = np.linspace(0, 2*np.pi, 17)', locals())

    R.sum()
    print_command('R.sum()', locals())
    R.min()
    print_command('R.min()', locals())
    R.max()
    print_command('R.max()', locals())

    print('# Sum of each column')
    A.sum(axis=0)
    print_command('A.sum(axis=0)', locals())

    print('# Min of each row')
    A.min(axis=1)
    print_command('A.min(axis=1)', locals())

    breakpoint()

    print_header('Universal Functions and Broadcasting')

    print('# Each universal function (which is usually a mathematical function like')
    print('# sin, cos, add, exp, etc.) takes array inputs and produces array outputs by')
    print('# performing the core function elementwise on the inputs. These operations are fast')

    A = np.random.random((8, 6))
    print_command('A = np.random.random((8, 6))', locals())
    B = np.random.random((8, 6))
    print_command('B = np.random.random((8, 6))', locals())

    print('# Return true if all elements meet criteria')
    print_command('np.all(A < 0.1)', locals())

    print('# Return true if any one element meets criteria')
    print_command('np.any(A < 0.1)', locals())


    print('# Return indices that would sort the array')
    print_command('np.argsort(A)', locals())
    print('# Actually sorts array')
    print_command('np.sort(A)', locals())

    # Reverse or permute axes of an array
    print_command('np.transpose(A)', locals())
    print_command('A.T', locals())

    breakpoint()

    print_header('Statistics')

    print('# Compute average. Can specify `weights` and `axis`')
    print_command('np.average(A)', locals())
    print_command('np.average(A, weights=np.linspace(0, 10, A.size).reshape(A.shape))', locals())
    print('# Compute arithmetic mean. Cannot specify `weights` but `axis` is still valid')
    print_command('np.mean(A)', locals())
    print_command('A.mean()', locals())

    print('# Compute the median. If `axis` is specified, then it will do so accordingly')
    print_command('np.median(A)', locals())

    print('# Compute standard deviation. Can specify `axis` and `dtype`')
    print_command('np.std(A)', locals())
    print('# Compute the variance. Ca nspecify `axis` and `dtype`')
    print_command('np..var(A)', locals())

    print('# Round up')
    print_command('np.ceil(A)', locals())
    print('# Round down')
    print_command('np.floor(A)', locals())
    print('# Round correctly')
    print_command('np.round(A)', locals())

    print('# Return the biggest element of the array')
    print_command('np.max(A)', locals())
    print_command('A.max()', locals())
    print('# Returns biggest element\'s index')
    print_command('np.argmax(A)', locals())
    print('# Elementwise maximum of two array\'s elements')
    print_command('np.maximum(A, B)', locals())

    print('# Return the smallest element of the array')
    print_command('np.min(A)', locals())
    print_command('A.min()', locals())
    print('# Return smallest element\'s index')
    print_command('np.argmin(A)', locals())
    print('# Elementwise minimum of two array\'s elements')
    print_command('np.minimum(A, B)', locals())

    print('# Add all the elements')
    print_command('np.sum(A)', locals())
    print_command('A.sum()', locals())

    print('# Multiply all the elements')
    print_command('np.prod(A)', locals())
    print_command('A.prod()', locals())

    print('# Remove values below or above certain value and substitute them')
    print_command('np.clip(A, 0.25, 0.75)', locals())

    breakpoint()

    print_header('Indexing, Slicing and Iterating')
    print('# One-dimensional array can be treated pretty much the same as a Python list')
    print('# Multi-dimensional arrays can have one index per axis, given as a tuple')
    print('# separated by commas')

    A = np.linspace(0, 10, 100).reshape(10, 10)
    A = A.round(1)
    print_command('A = np.linspace(0, 10, 100).reshape(10, 10)', locals())
    print_command('A = A.round(1)', locals())

    B = np.linspace(0,40, 40).reshape(5, 2, 4)
    B = B.round(1)
    print_command('B = np.linspace(0,40, 40).reshape(5, 2, 4)', locals())
    print_command('B = B.round(1)', locals())

    print_command('A[1]', locals())
    print_command('A[1,4]', locals())
    print_command('A[:5, 0]', locals())
    print('# The dots (...) represent as many colons as needed to produce a complete')
    print('# indexing tuple')
    print_command('A[:5, ...]', locals())
    print_command('A[:5, :]', locals())
    print_command('B[:2, ...]', locals())
    print_command('B[:2, :, :]', locals())

    breakpoint()

    print_header('Shape manipulation')

    A = np.linspace(0, 10, 100)
    A = A.round(1)
    print_command('A = np.linspace(0, 10, 100)', locals())
    print_command('A = A.round(1)', locals())

    print('# Change shape')
    print_command('A', locals())
    print_command('A.reshape(10, 10)', locals())
    print('# Using `resize` instead of `reshape` will change the original array')
    print('# Using -1 in the reshaping process will automatically assign other other dimensions')
    print_command('A.reshape(5, -1)', locals())
    print('# Flatten')
    print_command('A.ravel()', locals())
    print_command('np.array(A.flat)', locals())
    print('# Transpose')
    print_command('A.T', locals())
    print_command('np.transpose(A)', locals())

    print_header('Stacking different arrays')

    A = np.floor(10*np.random.random((2, 2)))
    print_command('A = np.floor(10*np.random.random((2, 2)))', locals())
    print_command('A', locals())
    B = np.floor(10*np.random.random((2, 2)))
    print_command('B = np.floor(10*np.random.random((2, 2))', locals())
    print_command('B', locals())

    print('# Vertical Stacking')
    print(np.vstack((A, B)))
    print('# Horizontal Stacking')
    print(np.hstack((A, B)))
    print('# Different from `hstack` with 1D arrays, where it sandwiches arrays on top')
    print('# of each other')
    print(np.column_stack((A.ravel(), B.ravel())))
    print('# Column stack\'s Transpose')
    print(np.row_stack((A.ravel(), B.ravel())))

    breakpoint()

    print_header('Splitting Arrays')
    A = np.floor(10*np.random.random((2, 12)))
    print_command('A = np.floor(10*np.random.random((2, 12)))', locals())

    print('# Split into 3')
    print_command('np.hsplit(A, 3)', locals())
    print('# Split after the third and fourth column')
    print_command('np.hsplit(A, (3, 4))', locals())

    breakpoint()

    '''
    print_header('Copies and Views')
    print('# Assigning and manipulating arrays in turn change the original array')
    a = np.arange(12)
    print_command('a = np.arange(12)', locals())
    print_command('a', locals())
    b = a
    print_command('b = a', locals())
    b.resize((3, 4))
    print_command('b.resize((3, 4))', locals())
    print_command('a', locals())

    print('# Instead use copies, which makes complete copies of the array and its data')
    d = np.arange(12)
    print_command('d = np.arange(12)', locals())
    print_command('d', locals())
    e = d.copy()
    print_command('e = d.copy()', locals())
    e.resize((3, 4))
    print_command('e.resize((3, 4))', locals())
    print_command('d', locals())
    print_command('e', locals())


    # Other math functions
    # https://numpy.org/doc/1.17/reference/ufuncs.html#math-operations

    



if __name__ == "__main__":
    main()

# Thank you
# https://numpy.org/devdocs/user/quickstart.html
# https://stackoverflow.com/questions/1277519/how-can-i-pass-my-locals-and-access-the-variables-directly-from-another-functio
