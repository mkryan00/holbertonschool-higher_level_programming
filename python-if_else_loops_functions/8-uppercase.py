#!/usr/bin/python3                                                                                                                                                              
def uppercase(str):
    new_str  = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            x = ord(char) - 32
            x = chr(x)
            new_str = new_str + x
        else:
            new_str = new_str + char
    print(new_str)
