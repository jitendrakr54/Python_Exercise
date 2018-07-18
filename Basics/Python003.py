#  write a program that prints out all the elements of the list that are less than 5.

def main():

    a = [6, 10, 30, 32, 12, 25, 35, 14, 15]

    b = []
    for element in a:
        if element % 5 == 0:
            # print(element)
            b.append(element)

    b.sort()
    print(b)

if __name__ == "__main__":
    main()