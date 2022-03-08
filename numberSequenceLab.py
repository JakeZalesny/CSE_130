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

def get_user_number() -> int: 
    number = int(input("Which francois number would you like to see? "))
    return number

def do_calculation(number) -> int:
    if number == 1 :
        value = 2
    elif number == 2 :
        value = 1
    
    else :
        f1 = 2
        f2 = 1 
        for index in range(3, number):
            value = f1 + f2 
            f1 = f2
            f2 = value
    return value

def main(): 
    number = get_user_number()
    value = do_calculation(number)
    print(f"Francois number {number} is {value}")

main()
