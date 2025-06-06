"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When the user enter a value that is not an integer
2. When will a ZeroDivisionError occur?
    When the user enters 0 in the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    By making a loop that says the denominator cannot be a zero
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (cannot be zero): "))

    while denominator ==0:
        print("Denominator can't be zero")
        print("Enter the valid denominator")
        denominator = int(input("Enter the denominator (cannot be zero): "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
