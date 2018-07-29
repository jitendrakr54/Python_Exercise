# some programs on array

from array import *
from numpy import *

def sortNumbers():
    val = array("i", [23, 21, 32, 14, 54])

    for i in range(len(val)):
        for j in range(len(val)-1-i):
            if val[j] > val[j+1]:
                temp = val[j]
                val[j] = val[j+1]
                val[j+1] = temp

    print(val)

def factorial():
    n = int(input("Enter no to find factorial"))

    f = 1
    for i in range(n, 1, -1):
        f = f*i

    print(f)

def createAndSearchArray():
    arr = array("i", [])
    length = int(input("Enter the length of array"))

    for i in range(length):
        val = int(input("Enter the next value"))
        arr.append(val)

    print(arr)

    valueToSearch = int(input("Enter the value for search"))

    k = 0
    for j in arr:
        if j == valueToSearch:
            print(str(valueToSearch) + " is at " + str(k) + " position")
            break
        k += 1
    if k == len(arr):
        print("Value doesn't exist")

    print(arr.index(valueToSearch))

def deleteFromArray():

    arr = array("i", [11, 22, 33, 44, 55])
    print(arr)

    position = int(input("Enter the element position to delete"))

    if position > len(arr):
        print("Deletion not possible")
    else:
        for i in range(position-1, len(arr)-1, 1):
            arr[i] = arr[i+1]

    for j in range(len(arr)-1):
        print(arr[j])
    print(arr)

def reverseArray():
    arr = array("i", [11, 22, 33, 44, 55])
    print(arr)
    revArray = array(arr.typecode, [])
    # start, stop, step
    for i in range(len(arr)-1, -1, -1):
        revArray.append(arr[i])

    print(revArray)

def useNumpy():
# array()
    # arr = array([1, 2, 3, 4, 5, 6])
    # arr = array([1, 2, 3, 4, 5, 6], int)
    # arr = array([1, 2, 3, 4, 5, 6.0])
    # arr = array([1, 2, 3, 4, 5, 6.0], int)
    # arr = array([1, 2, 3, 4, 5, 6], float)
    # print(arr)
    # print(arr.dtype)

# linspace()
    # arr = linspace(0, 15, 16)
    # print(arr)

# arange()
    # arr = arange(1, 15, 2)
    # print(arr)

# logspace()
    # arr = logspace(1, 10, 5)
    # print(arr)

# zeros()
    # arr = zeros(5)
    # arr = zeros(5, int)
    # print(arr)

# ones()
    # arr = ones(5)
    arr = ones(5, int)
    print(arr)

def findMax():
    arr = array([21, 83, 12, 23, 56, 22])

    max = 0

    for i in arr:
        if i > max:
            max = i

    print(max)

def multiDimArray():
    arr = array([
                    [1,2,3],
                    [4,5,6]
    ])

    arr1 = arr.flatten()
    print(arr)

    m = matrix('1,2,3 ; 4,5,6; 7,8,9')
    print(diagonal(m))