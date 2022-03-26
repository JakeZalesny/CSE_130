"""
Prime Number Program
"""

def get_desired_number() -> int:
    number = int(input("Enter desired number: "))
    return number

def do_calculation(number):
    lower = 0

    print("Prime numbers between", lower, "and", number, "are:")
    i = 0
    for num in range(lower, number + 1):
        print(f"#2 {num}, {i}")
        if num > 1:
            for i in range(2, num):
                print(f"#3 {num}, {i}")
                if (num % i) == 0:
                    print(f"#4 {num}, {i}")
                    break
            else:
                print(f"#5 {num}, {i}")
                print(num)

def main():
    number = get_desired_number()
    do_calculation(number)

main()
