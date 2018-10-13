#/usr/bin/env python
from random import randint, seed
from time import time

def standard_deviation(values_list):
    #Make sure values_list is only composed of numbers. If an instance of another datatype is found, ask to remove it. If it is not removed, return an error
    for value in values_list:
        if not isinstance(value,int) and not isinstance(value,float):
            correct_list_question = input("[!] Non-numerical value " + str(value) +" found. Remove from list?\n\t[user input]")
            if correct_list_question.lower() in ["y", "yes"]:
                values_list.remove(value)
            elif correct_list_question.lower() in ["n", "no"]:
                return "[!] Not all list values are numerical"
            else:
                return "[!] No valid response given. Program is exiting" 

    #Compute average
    average = sum(values_list)/len(values_list)

    #Compute standard deviation
    standard_deviation_calculation = ((sum([(value-average)**2 for value in values_list]))/len(values_list))**0.5

    return str("[*] Average = %f, Standard deviation = %f" % (average, standard_deviation_calculation))


if __name__ == "__main__":
    #Accept a series of comma-separated values from the user as a string 
    input_list = input("[*] Enter a list of numbers to find their average and standard deviation.\n\t[user input]")
    output_list = []

    if input_list.lower().strip() in ['random list', 'rl', 'random', 'r', '']:
         output_list = list(randint(1,100) for c in range(0,10))
         print("[*] Output list = " + str(output_list))

    else:
        #Strip any excess whitespace from this string and split it into a list elements originally separated by commas
        input_list = input_list.strip().split(',')
        
        #Loop through each element of the loop making sure only to extract numbers and appending them to the output_list
        for element in input_list[:]:
            element = element.strip().lower()
            if element.isdigit():
                output_list.append(float(element))

        print("[*] Output list = " + str(output_list))

    print(standard_deviation(output_list)) 
