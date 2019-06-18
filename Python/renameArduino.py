#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

def main():
    os.chdir("../Arduino/Instructional")

    # First loop through available tutorial examples
    for exampleFolder in os.listdir():
        name = str(exampleFolder).strip()
        home = os.getcwd()
        print(name)

        os.chdir(name)
        for project in os.listdir():
            print("\t" + project, end=" ... ")
            if re.match("^test.*", str(project).strip().lower()) and os.path.isdir(project):
                print("is project")
                sourceFile = "./{}/{}".format(project, os.listdir("./{}".format(project))[0])
                destinationFile = "{}.ino".format(name)
                os.rename(sourceFile, destinationFile)
                os.rmdir(project)

            else:
                print("is NOT project")

        os.chdir(home)





if __name__ == "__main__":
    main()