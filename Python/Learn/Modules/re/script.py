#!/usr/bin/env python
import re

read_data = ""
regular_expression = re.compile('Page\s*\d', re.IGNORECASE)
    
with open("text.txt", "r")  as in_file:
    read_data = in_file.read()
    read_data = str(read_data)

with open("text.txt", "w") as out_file:
    write_data = re.sub(regular_expression, "", read_data, re.M)
    print(write_data)
