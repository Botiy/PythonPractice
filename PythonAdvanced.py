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

