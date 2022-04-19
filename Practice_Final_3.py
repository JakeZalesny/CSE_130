

def get_list():
    _list = [
        25, 97, 34, 34, 76, 34, 64, 32, 46, 23, 12, 99
    ]
    return _list

def get_highest_subset(list): 

    sum_largest = list[0]
    for i in range(1, 5) :
        sum_last = sum_largest
        for i in range(6, len(list) - 1) : 
            sum_last += list[i] - list[i - 6] 

            if sum_last > sum_largest :
                sum_largest = sum_last
    print(int(sum_largest / 6))

list = get_list()
get_highest_subset(list)
