# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

def checkIfDivisible():
    dividend = int(input("Enter the dividend"))
    divisor = int(input("Enter the divisor now"))

    if dividend % divisor == 0:
        print(str(dividend) +" is divisible by "+ str(divisor))
    else:
        print("not divisible")
