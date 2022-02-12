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
    file_data = json.load(file_name)
    return file_data

def search_for_keyword(file_data, keyword, file_name) :
    length_of_data = len(file_data)
    
    if length_of_data / 2 != keyword :
        search_for_keyword(file_data / 2, keyword)
        search_for_keyword(file_data / 2, keyword)

    if length_of_data / 2 == keyword :
        print(f"We found {keyword} in {file_name}")
        return True
    
    else: 
        return False
