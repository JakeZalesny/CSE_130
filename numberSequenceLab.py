"""
# 1. Name:
#      Jake Zalesny
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      This program is meant to calculate the francois number of 
#      a user-inputed number
# 4. What was the hardest part? Be as specific as possible.
#      understanding what this program is actually supposed to calculate
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

"""
# Gets the desired number from the user and returns an int
def get_user_number() -> int: 
    number = int(input("Which francois number would you like to see? "))
    return number

# Calculates the francois nubmer based off of the user's input
def do_calculation(number) -> int:
    if number <= 0: 
        print("Error please enter a positive integer")
        return None

    elif number == 1 :
        value = 2
    
    elif number == 2 :
        value = 1
    
    else :
        f1 = 2
        f2 = 1 
        for index in range(2, number):
            value = f1 + f2 
            f1 = f2
            f2 = value
    return value

# Calls both functions and displays the message to the user. 
def main(): 
    number = get_user_number()
    value = do_calculation(number)
    if value is not None:
        print(f"Francois number {number} is {value}")

main()
