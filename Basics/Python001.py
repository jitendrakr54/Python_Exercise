# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

def main():
    name = input("Enter ur name")
    age = int(input("Enter ur age"))

    year = str((2014 - age)+100)

    print(name +" you will turn 100 in "+ year)

if __name__ == "__main__":
    main()