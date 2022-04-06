"""
CSE 130 Practice final #1

"""
import json


def get_filename():
    filename = input("What is the name of the file? ")
    return filename

def open_file(filename):
    with open(filename) as f :
        file = f.read()
        file = json.loads(file)
        data = file["array"]
        return data

def organize_data(data):
    top_bound = int(len(data) - 1)
    for i_up in range(0, int(top_bound / 2)):
        i_down = top_bound - i_up
        data[i_up], data[i_down] = data[i_down], data[i_up]
    
    for i in data :
        print(i, end=", \n")

def main(): 
    filename = get_filename()
    data = open_file(filename)
    organize_data(data)

main()