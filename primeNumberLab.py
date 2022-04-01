"""
Prime Number Program
# 1. Name:
#      Jake Zalesny
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      This assignment is meant to calculate all prime numbers within
#      a given boundary by eliminating early on factors. 
# 4. What was the hardest part? Be as specific as possible.
#      Figuring out how the algorithm actually worked was a bit complicated
#      I struggled to understand why it was done in a certain way in the 
#      instructor pseudocode but after looking a bit deeper into the functionality
#      of the code I finally grasped the concept a bit better.
# 5. How long did it take for you to complete the assignment?
#      1.0 hrs.
"""

def get_desired_number() -> int:
    """
    GET DESIRED NUMBER:
    ARGS:
    NO ARGUMENTS NECESSARY

    RTRNS:
    number (int) the desired upper bound as input by the user

    FUNCT:
    Gets the desired upper bound from the user and returns it
    as an integer
    """
    number = int(input("Enter desired number: "))
    return number


def do_calculation(number):
    """
    This is where the fun actually begins: 
    ARGS: 
    number (int): the desired upper bound as input by the user

    RTRNS: 
    NO RETURN VALUES

    FUNCT: 
    Finds a list of all prime values by eliminating early factors. 
    """

    if number <= 2:
        print("Please enter a real number greater than 2.")
        return
    
    numbers = []
    primes = []
    check_value = True
    for x in range(0, number + 1):
        numbers.append(check_value)
    
    numbers[0] = False
    numbers[1] = False
    
    assert(number == len(numbers) - 1)
    
    for factor in range(2, number + 1):
        assert(factor >= 2)
        if numbers[factor] :
            for multiple in range(factor * 2, number + 1, factor):
                numbers[multiple] = False

    assert(len(primes) == 0)        
    
    for index in range(2, number):
        if numbers[index]:
            primes.append(index)
    
    print(f"These are the prime values under {number} are: \n{primes}")


def main():
    """
    MAIN: 
    ARGS: 
    NO ARGUMENTS NECESSARY

    RTRNS: 
    NO RETURN VALUES

    FUNCT:
    Runs both functions as previously defined in the program
    """
    
    number = get_desired_number()
    do_calculation(number)

main()
