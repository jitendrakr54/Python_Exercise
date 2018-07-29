# Different types of pattern

def pattern1():
    for i in range(4):
        for j in range(4):
            print("*", end="")
        print()

def pattern2():
    for i in range(4):
        for j in range(i+1):
            print("*", end="")
        print()

def pattern3():
    for i in range(4):
        for j in range(4-i):
            print("*", end="")
        print()

def pattern4():
    for i in range(4):
        for j in range(i+1, 5):
            print(j, end="")
        print()

def pattern5():
    for i in range(4):
        for j in range(4):
            if i<j:
                print(chr(65+14+j), end="")
            else:
                print(chr(65+j), end="")
        print()