"""
# 1. Name:
    Jake Zalesny
# 2. Assignment Name:
    Lab 06: Advanced Search
# 3. Assignment Description:
    This program is meant to search through a list of words in a JSON format, provided 
    by the user to find a keyword.
# 4. Algorithmic Efficiency
    O(log n) efficiency
# 5. What was the hardest part? Be as specific as possible.
    Designing it to be O(log n) within the given time constraints
# 6. How long did it take for you to complete the assignment?
    4 hrs. 

"""
import json


def get_filename() :
    file_name = input("What is the name of the file? ")
    return file_name

def get_keyword() :
    keyword = input("What name are we looking for? ")
    return keyword

def get_file_data(file_name) :
    with open(file_name) as f :
        data = f.read()
        file_data = json.loads(data)
        array = file_data["array"]
    return array

def search_for_keyword(file_data, keyword, file_name) :
    # Checks to see if the list is empty
    if len(file_data) == 0 :
        print("The list is empty")
        return
    
    length_of_data = (int)(len(file_data) / 2)

    # This is the part of recursion and the constraints placed
    if file_data[length_of_data] != keyword :
        if length_of_data != 0 :
            if file_data[length_of_data] > keyword :
                return search_for_keyword(file_data[: length_of_data], keyword, file_name)

            elif file_data[length_of_data] < keyword :
                return search_for_keyword(file_data[length_of_data :], keyword, file_name)

    # If any one of these two cases is met it walks back up
    # the recursion string all the way up to it's initial call in main
    if file_data[length_of_data] == keyword :
        print(f"We found {keyword} in {file_name}")
        return True
    
    else :
        print(f"Error {keyword} not found")
        return False

# Calls each function and sets the variables up accordingly.         
def main() :
    file_name = get_filename()
    keyword = get_keyword()
    file_data = get_file_data(file_name)
    search_for_keyword(file_data, keyword, file_name)

main()
