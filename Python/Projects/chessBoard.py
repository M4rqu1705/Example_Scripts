black, white = '░', '▓'
rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
columns = [str(num) for num in range(8, 0, -1)]
previous = "black"
for i in range(8):
    print(rows[i] + " ", end='')
    for j in range(8):
        if previous == "black":
            print(white*3, end='')
            previous = "white"
        else:
            print(black*3, end='')
            previous = "black"
    print("")
    previous = "black" if previous == "white" else "white"

print( ' '*3 +  '  '.join(columns) )
