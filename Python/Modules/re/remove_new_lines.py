#!/usr/bin/pythn

read_data = ""

with open("text.txt", "r" , encoding='utf-8') as in_file:
    read_data = str(in_file.read())

with open("text.txt", "w", encoding='utf-8') as out_file:
    #  write_data = read_data.replace('\n\n', '<this_was_a_double_newline>').replace('\n', ' ').replace('\r', '').replace("<this_was_a_double_newline>", '\n\n')
    write_data = read_data.replace('\n',' ')
    #  print(write_data)

    out_file.write(write_data)