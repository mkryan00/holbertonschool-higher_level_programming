#!/usr/bin/python3
def safe_print_division(a, b):
    res = None
    # initialise res = None - when b = 0.
    # Without it, the except block would set nothing.
    # Finally would try to print res which hasn't be assigned.
    # (NameError)
    try:
        res = a/b
    except ZeroDivisionError:
        pass
    # Dividing by 0 gives you ZeroDivisionError exception in Python.
    finally:
        print("Inside result: {}".format(res))
        return (res)
