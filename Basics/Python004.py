# To check greatest from three user input

def greatestFromThreeNo():
    a = int(input("Enter three nos"))
    b = int(input())
    c = int(input())

    msg = " is greatest of all three!"
    if a > b:
        if a > c:
            print(str(a) + msg)
        else:
            print(str(c) + msg)
    elif b > a:
        if b > c:
            print(str(b) + msg)
        else:
            print(str(c) + msg)
    else:
        print(str(c) + msg)