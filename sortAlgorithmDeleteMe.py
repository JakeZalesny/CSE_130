"""
# 1. Name:
#      Jake Zalesny
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This assignment is meant to sort the list into an ascending order
# 4. What was the hardest part? Be as specific as possible.
#      Figuring out how to write an efficient bubble sort was
#      relatively challenging. 
# 5. How long did it take for you to complete the assignment?
#      2 hours

"""

"""
Had to import the json library in order to read the json file. 
"""
import json

"""
This function retrieves the file name based on the user's input and 
returns it. 
"""

def get_filename():
    file_name = input("What is the name of the file? ")
    return file_name

"""
This function retrieves the data from the file and opens it,
the data is then stored under the array variable and it is returned
"""

def get_file_data(file_name) :
    with open(file_name) as f :
        data = f.read()
        _list = json.loads(data)
        array = _list["array"]
    return array

"""
This function sorts the array and it's set to return a string
It does so by iterating through in what's called a bubble sort 
pattern, moving things lower than the current value to the left
and moving things higher to the right. 
"""

def sort_list(array, file_name) -> str :
    if len(array) == 0 :
        print("The file is empty!")
        return
    n = len(array)

    for i in range(n - 1) : 
        assert(n < i, "Iteration Error")       
        for j in range(0, n - i - 1) :             
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]
                assert(array[j] != array[j + 1], "Duplication Error!")
    
    print(f"\nThe values in {file_name} are: ")
    for l in array :
        print(f"\t{l}")
    
"""
Main is where everything is called and arranged and where the program
is ran. 
"""

def main() :
    file_name = get_filename()
    array = get_file_data(file_name)
    sort_list(array, file_name)
    
# Runs the Program
main()

