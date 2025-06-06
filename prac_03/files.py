"""
1. Write code that asks the user for their name, then open a file called name.txt and writes that name to it. Use open
and close for this question
"""

name = input("Your name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

"""
2. In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name 
(as above) then prints (note the exact output). Do not simply print the user's input variable!. 
Use open and close for this question
"""

second_file = open("name.txt", 'r')
name = second_file.read().strip()
print(f"Greetings {name}!")
second_file.close()

"""
3. Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate
lines in the file and save it:
a. 17
b. 42
c. 400
"""

with open("numbers.txt", 'r') as third_file:
    first_number = int(third_file.readline())
    second_number = int(third_file.readline())
    print(first_number + second_number)

"""
4. Now write a fourth block of code that prints the total for all line in number.txt. This should work for a file with 
any number of numbers. Use with instead of open and close for this question.
"""

total_number = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        number = int(line)
        total_number += number
print(total_number)
