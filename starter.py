# PROBLEM 1
# Create a variable that holds the value of your first name.
firstName = 'James'

# PROBLEM 2
# Create a variable that holds the value of your favorite number.
favoriteNumber = '7'

# PROBLEM 3
# Create a variable that holds a boolean value representing if your hair is brown.
isBrown = False

# PROBLEM 4
# Print your first name, by printing the variable created in problem 1.
print(firstName)

# PROBLEM 5
#  Create a variable called `loves_code` and set it equal to true. 
#  Check to see if `loves_code` is equal to true or false. 
#  If it is true, print "I love to code!"
#  If it is not, print "Coding has its challenges."
loves_code = True
if loves_code:
    print('I love to code!')
else:
    print('Coding has its challenges.')


# PROBLEM 6
# Create a list called `colors` and set it equal to a list of at least five colors.
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


# Problem 7
# Using bracket syntax, print out the last item in your colors list.
print(colors[len(colors) - 1])

# For problems 8-9, use the following line of code:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Problem 8
# Use a for-in loop to iterate over the `numbers` list and print each number.
for num in numbers:
    print(numbers[num-1])


# Problem 9
# Create an empty list called `even_numbers`.
# Use a for-in loop to iterate over the `numbers` list, and if a number is even, add  it to the `even_numbers` list.
even_numbers = []

for num in numbers:
    number = numbers[num-1]
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# Problem 10
# Do not edit the code below.
score = 74
# Do not edit the code above.

# Determine if the letter grade of the given variable 'score'. If the variable is a 90 or above, console-log an 'A', between 80 and 89, console-log a 'B', 
# between 70 and 79, 'C', between 60 and 69, 'D', and anything below 60 should console-log an 'F'.


def getLetterGrade(score):
    if score > 90:
        print('A')
        return
    if score > 80:
        print('B')
        return
    if score > 70:
        print('C')
        return
    if score > 60:
        print('D')
        return
    if score > 0:
        print('F')

getLetterGrade(score)