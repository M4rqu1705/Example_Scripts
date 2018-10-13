#!/usr/bin/python

read_data = ""

with open("text.txt", "r") as in_file:
    read_data = in_file.read()
    read_data = str(read_data)

with open("text.txt", "w") as out_file:
    write_data = read_data.replace('\n\n', '<this_was_a_double_newline>').replace('\n', ' ').replace('\r', '').replace("<this_was_a_double_newline>", '\n\n')
    #  print(write_data)

    out_file.write(write_data)
