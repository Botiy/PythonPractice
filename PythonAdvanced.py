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

magic()

