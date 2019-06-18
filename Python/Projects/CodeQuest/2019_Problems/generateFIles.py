import os


filename = "Prob"

code = '''#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline().strip())

lines = []

for c in range(T):
    lines.append(sys.stdin.readline().strip())

# --- Your code goes here ---



# --- Your code goes here ---
'''

for c in range(20):
    local_dirname = filename + "{:02.0f}".format(c)
    if not os.path.exists(local_dirname):
        # Create directory
        os.mkdir(local_dirname)

        # Create files
        _filename = local_dirname + "/" + local_dirname + ".py"
        _samplename = local_dirname + "/sample-" + local_dirname + "1.in"
        with open(_filename, "+w") as f:
            f.write(code)

        # Copy example inputs 
        if os.path.exists("C:/Users/m4rc0/Downloads/sample-" + local_dirname + "1.in"):
            data = ""
            with open("C:/Users/m4rc0/Downloads/sample-" + local_dirname + ".in", "r") as f:
                data = ''.join(f.readlines())

            with open(_samplename, "+w") as f:
                f.write(data)




