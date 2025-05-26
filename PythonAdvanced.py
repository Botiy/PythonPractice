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

#iteration('Boti', 23, 195)

def sum_counter():
    nl = [0,1,2,3,4,5,6,7,8,9,10]

    count = 0
    for item in nl:
        count += item
        print(count)

#sum_counter()

# Start, stop, stepover
def range_function(min,max,jump):
    for numbers in range(min,max,jump):
        print(numbers)
'''

print("Let's create a range of numbers!")
print("Enter the starting number (inclusive):")
min_input = int(input())

print("Enter the ending number (exclusive):")
max_input = int(input())

print("Enter the step size (positive or negative):")
jump_input = int(input())

range_function(min_input, max_input, jump_input)
'''

'''
Duplicate search
'''

def duplicate_search():
    mlist = ['a', 'v', 'c', 0, 4, 44, 3, 0, 15, 'c', 'c', 'Janos', 'Janos']

    duplicates = []
    for item in mlist:
        if mlist.count(item)>1:
            if item not in duplicates:
                duplicates.append(item)

    print(duplicates)

#duplicate_search()

'''
Highest even
'''

def highest_even(custom_list):
    evens = []
    for item in custom_list:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

#print(highest_even([2,5,12,32,432,234113,123,1223,1444,2002]))

'''
Prime
'''
def prime(number):
    '''
    Tells whether an input number is a prime number or not.
    :param number: The input number.
    :return:
    '''
    if int(number) % 2 == 0:
        print(f"{number} is not a prime number!")
        return
    else:
        count = 3
        while count < (int(number) / 2):
            if int(number)%count==0:
                print(f"{number} is not a prime number!")
                return
            count += 1
        print(f"{number} is a prime number!")
        return

#prime(input())

'''
Primes in a range
'''

def range_prime(min, max):
    '''
    Shows whether numbers are prime or not within the given range.
    :param min: Beginning
    :param max: End
    :return: None
    '''
    for number in range(int(min), int(max)):
        if number < 2:
            print(f"{number} is not a prime number!")
            continue
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):  # Only check up to square root
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{number} is a prime number!")
        else:
            print(f"{number} is not a prime number!")

# Prompt user input and run
range_prime(input("Enter minimum number: "), input("Enter maximum number: "))
