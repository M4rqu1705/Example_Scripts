with open("Prob02.in.txt") as f:
    read_data = f.readlines()
    T = int(read_data.pop(0).strip())
    for data in read_data:
        print(data.count('a') + data.count('e') + data.count('i') + data.count('o') + data.count('u'))

