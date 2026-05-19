#!/usr/bin/python3
def max_integer(my_list=[]):

    res = my_list[0]
    for n in my_list:
        if n > res:
            res = n
            return(res)
