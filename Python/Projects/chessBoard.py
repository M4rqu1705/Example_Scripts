#!/usr/bin/env python
# -*- coding: utf-8 -*-

def generateCheckeredBoard():
    black, white = '░', '▓'
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rows = [str(num) for num in range(8, 0, -1)]
    cellWidth = 3
    board = ""
    previous = "black"

    # Begin by adding column labels
    board += '  ' + ' ' * (cellWidth//2) + str(' ' * (cellWidth-1)).join(columns)
    board += "\n"

    # Build row by row
    for i in range(8):
        # Add row label
        board += rows[i] + " "
        # Add cells
        for j in range(8):
            if previous == "black":
                board += white * cellWidth
                previous = "white"
            else:
                board += black * cellWidth
                previous = "black"
        # Add row label again
        board += " " + rows[i]
        # End line
        board += "\n"
        previous = "black" if previous == "white" else "white"

    # End by adding column labels again
    board += '  ' + ' ' * (cellWidth//2) + str(' ' * (cellWidth-1)).join(columns)
    board += "\n"

    return board


if __name__ == "__main__":
    print(generateCheckeredBoard())
