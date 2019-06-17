#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def main():
    pwd = os.getcwd()
    filename = "Prob_"
    content = '#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nwith open() as f:\n\tread_data = f.read_lines()\n\tT = read_lines.pop(0)\n'

    for c in range(1,21):
        directoryName = pwd + "\\" + filename + str(c)
        if not os.path.exists(directoryName):
            os.mkdir(directoryName)

        temp = directoryName + "\\" + filename + str(c) + ".py"
        temp = temp.replace("\\\\", "\\")
        print(temp) 
        with open(temp, "w+") as f:
            f.write(content)




if __name__ == "__main__":
    main()
