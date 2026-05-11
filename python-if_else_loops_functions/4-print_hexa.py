#!/usr/bin/python3
for num in range(99):

    hex_value = "{0:x}".format(num)

    print(f"{num}", "=", f"0x{hex_value}")
