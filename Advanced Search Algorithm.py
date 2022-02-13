"""
Advanced Search algorithm
Jake Zalesny

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
    length_of_data = (int)(len(file_data) / 2)
    if file_data[length_of_data] != keyword :
        if length_of_data != 0 :
            if file_data[length_of_data] > keyword :
                search_for_keyword(file_data[: length_of_data], keyword, file_name)
            
            elif file_data[length_of_data] < keyword :
                search_for_keyword(file_data[length_of_data :], keyword, file_name)

    if file_data[length_of_data] == keyword :
        print(f"We found {keyword} in {file_name}")
        return True
    
    else: 
        return False
    
def main() :
    file_name = get_filename()
    keyword = get_keyword()
    file_data = get_file_data(file_name)
    search_for_keyword(file_data, keyword, file_name)

main()
