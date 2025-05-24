import math
try:
    number = float(input("Enter a number: "))

    square = math.sqrt(number)
    log = math.log(number)
    sine = math.sin(number)

    print(f"\nResults for the number {number}:")
    print(f"Square root: {square}")
    print(f"Natural logarithm (log base e): {log}")
    print(f"Sine (in radians): {sine}")
except:
    print("valid number")
