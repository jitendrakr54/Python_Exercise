#Program for Perfect square

import math

def perfectSquare():

    l = []
    for i in range(1, 100):
        for j in range(0, i+1):
            m = j*j
            if m > i:
                break
            if i == m:
                l.append(i)
    return l

def perfectSquares():
    l = []
    for i in range(1, 500, 1):
        if i**2 <= 500:
            l.append(i**2)
        else:
            break
    return l

def checkIfPerfectSquare():
    n = int(input("Enter any no"))

    for i in range(1, n+1):
        mult = i*i
        if mult > n:
            break
        if mult == n:
            print("YES")
            return

    print("NO")