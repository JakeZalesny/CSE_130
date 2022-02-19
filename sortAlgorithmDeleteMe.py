"""
Ascending Sort test

"""

def get_list() :
    
    _list = [31, 72, 10, 32, 18, 95, 25, 50]
    return _list

def sort_list(_list) -> str :
    n = len(_list)
    tis = []
    ns = []
    js = []
    _listjs = []
    _listjs1 = []
    j = 0

    for i in range(n - 1) :
        tis.append(i)
        js.append(j)
        ns.append(n)
        _listjs.append(_list[j])
        _listjs1.append(_list[j + 1])
        for j in range(0, n - i - 1) :
            tis.append(i)
            js.append(j)
            ns.append(n)
            _listjs.append(_list[j])
            _listjs1.append(_list[j + 1]) 
            
            if _list[j] > _list[j + 1] :
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
            tis.append(i)
            js.append(j)
            ns.append(n)
            _listjs.append(_list[j])
            _listjs1.append(_list[j + 1])
    
    print(_list) 
    for i in range(len(tis)) :
        print(tis[i], js[i], ns[i], _listjs[i], _listjs1[i],"\n")


def main() :
    _list = get_list()
    sort_list(_list)

main()

