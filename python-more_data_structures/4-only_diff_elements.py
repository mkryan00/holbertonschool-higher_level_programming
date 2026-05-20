#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res1 = list(set(set_1) - set(set_2))
    res2 = list(set(set_2) - set(set_1))

    res = res1 + res2
    return (res)
