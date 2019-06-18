with open("Prob01.in.txt") as inputs:
    lines_list = inputs.readlines()
    T = int(lines_list[0].strip())
    for i in range(1, T+1):
        if int(lines_list[i].strip()) < 70:
            print("FAIL")
        ele:
            print("PASS")
