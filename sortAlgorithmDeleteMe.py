"""
Ascending Sort test

"""
from array import array
from fileinput import filename
import json

def get_filename():
    file_name = input("What is the name of the file?")
    return file_name

def get_file_data(file_name) :
    with open(file_name) as f :
        data = f.read()
        _list = json.loads(data)
        array = _list["array"]
    return array

def sort_list(array) -> str :
    n = len(array)

    for i in range(n - 1) :        
        for j in range(0, n - i - 1) :             
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]
    


def main() :
    file_name = get_filename()
    array = get_file_data(file_name)
    sort_list(array)
    
    print(f"The values in {file_name} are: ")
    for language in array :
        print(f"\t{language}") 

main()

