import re

with open("Prob03.in.txt") as f:
    read_data = f.readlines()
    T = read_data.pop(0)
    for data in read_data:
        data = data.strip()
        data = re.sub("(\d+).*?$", "\\1th", data)
        if(int(data[0]) > 1):
            data = re.sub("1[\D]*?$", "1st", data)
            data = re.sub("2[\D]*?$", "2nd", data)
            data = re.sub("3[\D]*?$", "3rd", data)
        print(data)

        
