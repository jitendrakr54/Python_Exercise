#  write a program that prints out all the elements of the list that are divisible by no.

def printDivisibleByInputedNo():

    a = [6, 10, 30, 32, 12, 25, 35, 14, 15]
    i = int(input("Enter ur no"))

    b = []
    for element in a:
        if element % i == 0:
            # print(element)
            b.append(element)

    b.sort()
    print(b)
