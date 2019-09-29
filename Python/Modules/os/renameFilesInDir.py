#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def main():
    # Your code starts here ---------------------------------------------------

    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        try:
            f_num, f_title = f_name.split('-')

            f_num = str(f_num).zfill(2)

            f_title = f_title.strip().title()
            while f_title.endswith("."):
                f_title = f_title[:-1]

            f_ext = ".php"
        except:
            continue

        file_name = "{}-{}{}".format(f_num,f_title,f_ext)

        os.rename(f, file_name)



    # Your code ends here -----------------------------------------------------


if __name__ == "__main__":
    main()

