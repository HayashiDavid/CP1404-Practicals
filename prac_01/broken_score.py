"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

# Original Code
# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")

"""
Things that needs fixing:
Inefficient if else structure 
print line is not indented 
redundant checking for if score > 100 after the else statement
"""

# Fixed Code
score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
