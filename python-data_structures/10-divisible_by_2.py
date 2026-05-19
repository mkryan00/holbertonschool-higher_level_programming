#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    results = []
    for n in my_list:
        if n % 2 == 0:
            results.append(True)
        else:
            results.append(False)
    return (results)
