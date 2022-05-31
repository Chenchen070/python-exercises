# 1. Conditional Basics
# a. prompt the user for a day of the week, print out whether the day is Monday or not

day_of_the_week = input('Today is:')
if day_of_the_week == 'Monday':
    print('Monday')
else:
    print('Not Monday')

# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
today = input('Today is:')
if today == ('monday','tuesday','wednesday','thursday','friday'):
    print('weekday')
else:
    print('weekend')

# c. create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
hours = input('Enter hours:')
rates = input('Enter rates:')
h = float(hours)
if h <= 40 :
    pay = h * float(rates)
else:
    overtime = h - 40
    pay = (40 * float(rates)) + (float(overtime) * (float(rates) * 1.5))
print (pay)

# Loop Basics
# a. While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i < 1000000:
    print(i)
    i *= i

# Write a loop that uses print to create the output shown below.
i = 100
while i >= 5:
    print(i)
    i -= 5

# b. For Loops
# i.Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
number = input('Pick a number:')
for i in range(1,11):
    print(number + 'x' + str(i) + '=' + str((int(number) * i)))
    i += 1

# ii. Create a for loop that uses print to create the output shown below.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
for number in range(1,2):
    for x in (1,11,111,1111,11111,111111,1111111,11111111,11111111):
        y = number * x
        print(y)
        number += 1

# break and continue
# i.Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
number = input('Please input a odd number between 1 to 50:')
print('Number to skip is:' + str(number))

for n in range(1,51):
    if n % 2 == 0:
        continue
    print(f'Here is an odd number: {n}')
    if n == number:
        print('Yikes! Skipping number:' + str(number))


# d. Prompt the user to enter a positive number and write a loop that counts from 0 to that number.
n = input('Enter a positive number:')
i = 0
while i <= int(n):
    print(i)
    i += 1

# e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
n = input('Enter a positive integer:')
i = int(n)
while i >= 1:
    print(i)
    i -= 1

# 3. Fizzbuzz
# Write a program that prints the numbers from 1 to 100.
#For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# 4. Display a table of powers.
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

def main():
    start = 1
    end = int(input('What number would you like to go up to?:'))
    print('Here is your table!')
    print('number','squared','cubed')

    for i in range(1,end+1):
        print (i,i**2,i**3)
        i += 1
    
    while True:
        ask = input('Would you like to continue? yes/no')
        if ask == 'yes':
            end = int(input('What number would you like to go up to?:'))
            for i in range(1,end+1):
                print (i,i**2,i**3)
                i += 1
        if ask == 'no':
            print('Bye!')
            break
        else:
            print('Enter either yes/no')
main()

# 5. Convert given number grades into letter grades.
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

def main():
    score = input('What is your score?:')
    x = int(score)

    if x > 0 and x < 60:
        print('Grade range: F')
    elif x >= 60 and x < 67:
        print('Grade range: D')
    elif x >= 67 and x < 80:
        print('Grade range: C')
    elif x >= 80 and x < 88:
        print('Grade range: B')
    elif x >= 88 and x <= 100:
        print('Grade range: A')
    else:
        print('Please enter a valid number')

    while True:
        ask = input('Would you like to continue? yes/no')
        if ask == 'yes':
            score = int(input('What is your score?:'))
            x = int(score)

            if x > 0 and x < 60:
                print('Grade range: F')
            elif x >= 60 and x < 67:
                print('Grade range: D')
            elif x >= 67 and x < 80:
                print('Grade range: C')
            elif x >= 80 and x < 88:
                print('Grade range: B')
            elif x >= 88 and x <= 100:
                print('Grade range: A')
            else:
                print('Please enter a valid number')
            
        if ask == 'no':
            print('Bye!')
            break
        else:
            print('Enter either yes/no')
main()

# 6.Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
# a. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
library = [
    {'title': 'Magic Tree House',
    'author': 'A',
    'genre': 'fiction'},
    {'title': 'Harry Potter',
    'author': 'J',
    'genre': 'fantasy'},
    {'title': 'Marvel',
    'author': 'D',
    'genre': 'super hero'}
]
for books in library:
    print(books)

user_genre = input('Which genre do you want?:')
for book in library:
    if user_genre == book['genre']:
        print(book)