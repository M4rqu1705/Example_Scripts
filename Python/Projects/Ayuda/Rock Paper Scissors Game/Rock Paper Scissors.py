#1)import required modules
#1a) Import csv
import csv
#1b) Import matplotlib
import matplotlib.pyplot as plt
import os.path
#1c) Import random
import random


#2) Create a list with the strings "rock", "paper", "scissors"
alternatives = ["rock", "paper", "scissors"]


#3) Read history file
history = []
# https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
if os.path.isfile("history.csv"):           #only extract contents if file is found
    with open("history.csv", "r+") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            history.append(row)


#4) Welcome the user
print("Welcome to the game of 'Rock, Paper, Scissors'!!")
print("Enter 'rock', 'paper', or 'scissors' to make your move.")
print("="*80)


#5) Begin loop
response = ""
while response != "no":
    #5a) Generate the computer's answer
    computer = random.choice(alternatives)
    #5b) Input the user's answer
    response = input("What will you play? Rock, paper, or scissor?: ").strip().lower()

    result = ""
    #5c) If the computer's answer is equal to the user's answer, it is a draw
    if computer == response:
        result = "Draw"
    #5d) If the computer's answer is rock and the user's answer is paper, the user won
    elif computer == "rock" and response == "paper":
        result = "You win"
    #5e) If the computer's answer is rock and the user's answer is scissor, the computer won
    elif computer == "rock" and response == "scissors":
        result = "You lose"
    #5f) If the computer's answer is paper and the user's answer is scissor, the user won
    elif computer == "paper" and response == "scissors":
        result = "You win"
    #5g) If the computer's answer is paper and the user's answer is rock, the computer won
    elif computer == "paper" and response  == "rock":
        result = "You lose"
    #5h) If the computer's answer is scissors and the user's answer is rock, the user won
    elif computer == "scissors" and response == "rock":
        result = "You win"
    #5i) If the computer's answer is scissors and the user's answer is paper, the computer won
    elif computer == "scissors" and response == "paper":
        result = "You lose"
    #5j) If the user misspells any word, collect user answer again
    elif response not in alternatives:
        print("Not a valid answer. Please try again!")
        continue


    #5k) Store results
    history.append([response, computer, result])

    #5l) Give user feedback
    print("Computer used " + str(computer))
    print(response)
    print()
    print("Do you want to play again?")
    response = input("(Enter 'no' to exit program): ").strip().lower()
    print("="*80)


#6) Store history to output file
# https://stackoverflow.com/questions/4842956/python-how-to-remove-empty-lists-from-a-list
history = [x for x in  history if x != []]
with open("history.csv", "w+") as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in history:
        csv_writer.writerow(row)


#7) Graph summary of history
#7a) Prepare data
frequency = [0, 0, 0]
computer_frequency = [0, 0, 0]
wins = []
# https://python-graph-gallery.com/3-control-color-of-barplots/
wins_colors = []
#extract data to frequency, computer_frequency, wins, and wins_colors variables to later be graphed
for entry in history:
    if entry[0] == "rock":
        frequency[0] += 1
    elif entry[0] == "paper":
        frequency[1] += 1
    elif entry[0] == "scissors":
        frequency[2] += 1

    if entry[1] == "rock":
        computer_frequency[0] += 1
    elif entry[1] == "paper":
        computer_frequency[1] += 1
    elif entry[1] == "scissors":
        computer_frequency[2] += 1

    if entry[2] == "You win":
        wins.append(2.0)
        wins_colors.append("green")
    elif entry[2] == "Draw":
        wins.append(1.0)
        wins_colors.append("blue")
    else:
        wins.append(0.1)
        wins_colors.append("red")

# https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/subplot.html
#7b) Plot user's answers frequency table
plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.subplot(2,2,1)
plt.bar(alternatives, frequency, align='center', color="green")
plt.title("Frequency of user moves")

#7c) Plot computer's answers frequency table
plt.subplot(2,2,3)
plt.bar(alternatives, computer_frequency, align='center', color="red")
plt.title("Frequency of computer moves")

#7d) Plot history of wins, losses and ties
plt.subplot(2,2,2)
plt.bar(list(range(len(wins))), wins, color=wins_colors)
plt.yticks([0.1, 1.0, 2.0], ["Lose", "Draw", "Win"])
plt.title("Win / Loss History")

plt.show()
