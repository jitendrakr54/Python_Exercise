# print first 50 fibonacci

def fibonacci():
    n = int(input("Enter no of series"))

    first = 0
    second = 1
    next = 0
    for i in range(1, n):
        print(str(first), end=" ")
        next = first + second
        first = second
        second = next

def fibonaccis():
    n = int(input("Enter till no of series"))

    first = 0
    second = 1
    next = 0
    print("0 1",end=" ")
    for i in range(1, 10):
        next = first + second
        first = second
        second = next
        if(next <= 10):
            print(str(next), end=" ")
        else:
            break