#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def generate_possible_moves(gamestate):
    all_states = []
    character = "*"
    if gamestate.count("X") == gamestate.count("O"):
        character = "X"
    else:
        character = "O"

    # Get index of every space
    spaces_index = []
    for c in range(9):
        if gamestate[c] == "*":
            spaces_index.append(c)

    for c in spaces_index:
        new_gamestate = gamestate[:]
        new_gamestate = new_gamestate[0:c] + character + new_gamestate[c+1:]
        all_states.append(new_gamestate)

    return all_states


def determine_winner(gamestate):
    winning = [r'X..X..X', r'X...X...X', r'..X.X.X..', r'...XXX...',r'XXX......', r'......XXX',  ]
    losing = [r'O..O..O', r'O...O...O', r'..O.O.O', r'...OOO...',r'OOO......', r'......OOO',  ]
    if any([re.match(winning[c], gamestate) for c in range(len(winning)) ]):
        return 1
    elif any([re.match(losing[c], gamestate) for c in range(len(losing)) ]):
        return -1
    elif gamestate.count("*") != 0:
        return 2
    else:
        return -1


def tictactoe(gamestate):

    state = determine_winner(gamestate)

    if -1 <= state <= 1:
        return(state)

    x = []
    for move in generate_possible_moves(gamestate):
        x.append(tictactoe(move))

    return sum(x)


def main(gamestate):

    choices = []
    moves = generate_possible_moves(gamestate)
    for move in moves:
        choices.append(tictactoe(move))

    output = moves[choices.index(max(choices))]

    x = ""
    for c in range(0,len(output),3):
        x += output[c:c+3] + "\n"

    return x


def play():
    data = "*********"
    while determine_winner(data) == 2:
        print(main(data), end='')
        data = ''.join([input().strip(), input().strip(), input().strip()]).upper()
        print()


def test():
    with open('Prob17.in.txt') as f:
        read_data = f.readlines()
        T = read_data.pop(0)

        for c in range(0, len(read_data), 3):
            data = ''.join([read_data[c].strip(), read_data[c+1].strip(), read_data[c+2].strip()]).upper()

            print(main(data), end='')

play()
