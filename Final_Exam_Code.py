


def get_list() -> list:
    name_list = [
        "Jacob", "John", "Anthony", "Timothy", "Aaron", "Jacob", "John", "Tristan", "Thomas"
    ]
    return name_list

def sort_list(name_list):
    new_list = []
    for i in name_list :
        if i not in new_list :
            new_list.append(i)

    print(new_list)

def main() :
    name_list = get_list()
    sort_list(name_list)

main()