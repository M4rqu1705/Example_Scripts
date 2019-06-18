#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def main():
    pwd = os.getcwd()
    name = "Prob21r1_"

    content = '#!/usr/bin/env python\n\
# -*- coding: utf-8 -*-\n\
\n\
def main():\n\
    # Your code starts here ---------------------------------------------------\n\
    T = int(input())\n\
    for c in range(T):\n\
    \n\
    # Your code ends here ---------------------------------------------------\n\
\n\
if __name__ == "__main__":\n\
    main()'

    for c in range(1,21):
        directory_name = pwd + "\\" + name + str(c)
        if not os.path.exists(directory_name):
            os.mkdir(directory_name)

        full_path = directory_name + "\\" + name + str(c) + ".py"
        full_path = full_path.replace("\\\\", "\\")
        print(full_path) 
        with open(full_path, "w+") as f:
            f.write(content)



if __name__ == "__main__":
    main()
