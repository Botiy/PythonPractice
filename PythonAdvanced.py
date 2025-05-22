'''
Conditional logic
'''
def magic():
    print("Are you a wizard?")
    wizard = bool(input())
    print("Are you an expert?")
    expert = bool(input())

    if wizard and expert:
        print("Wizard and expert")
    elif wizard:
        print("Wizard")
    elif expert:
        print("Expert")
    else:
        print("Neither")

#magic()

'''
Loops
'''
# iterable: list, dictionary, tuple, set, string
# iteratre: one by one check each item

def iteration(name, age, height):
    person = {
        'name': name,
        'age': age,
        'height': height
    }
    for item in person.items():
        print(item)

iteration('Boti', 23, 195)

def sum_counter():
    nl = [0,1,2,3,4,5,6,7,8,9,10]

    count = 0
    for item in nl:
        count += item
        print(count)

sum_counter()

# Start, stop, stepover
def range_function(min,max,jump):
    for numbers in range(min,max,jump):
        print(numbers)

print("Let's create a range of numbers!")
print("Enter the starting number (inclusive):")
min_input = int(input())

print("Enter the ending number (exclusive):")
max_input = int(input())

print("Enter the step size (positive or negative):")
jump_input = int(input())

# --- Run the function with user inputs ---
range_function(min_input, max_input, jump_input)

