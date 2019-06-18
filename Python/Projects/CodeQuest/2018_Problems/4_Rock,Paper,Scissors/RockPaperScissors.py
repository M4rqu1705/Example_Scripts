with open("Prob04.in.txt") as f:
    read_data = f.readlines()
    T = read_data.pop(0)
    for case in read_data:
        case = case.strip()
        if 'R' in case and 'S' in case and 'P' in case:
            print("NO WINNER")
        elif 'R' in case and 'S' in case:
            if case.count('R') > 1:
                print("NO WINNER")
            else:
                print("ROCK")
        elif 'P' in case and 'R' in case:
            if case.count('P') > 1:
                print("NO WINNER")
            else:
                print("PAPER")
        elif 'S' in case and 'P' in case:
            if case.count('S') > 1:
                print("NO WINNER")
            else:
                print("SCISSORS")
        else:
            print("NO WINNER")



