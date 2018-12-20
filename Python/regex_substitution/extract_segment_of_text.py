# Import the re module. It will be extensively used in this program
import re

# Import the Tkinter module. It will be used to copy text to clipboard
try:
    from Tkinter import Tk
except ImportError:
    from tkinter import Tk

# Create Tk object
tk_object = Tk()

tk_object.withdraw()


# Create variable read_data at global scope
read_data = ""

# Open the desired file in read-only mode
with open("OReilly Learning VIM 7th.txt", 'r', encoding='utf-8') as in_file:
    # Read the contents of the file and store them as string
    read_data = in_file.read()

# Remove any extraneous character from file
    # https://www.freeformatter.com/regex-tester.html

read_data = re.sub(r"[^\!\@\#\$\%\^\&\*\(\)\_\-\+\=\{\}\[\]\\\|\:\"\;\'\<\,\>\.\?\/\w\d\s]*", "", read_data)

# Make sure to leave appropriate spaces where there were previously newlines
read_data = re.sub(r"\n", " ", read_data)

# Create variable to store the indices to the text to extract
index = [0, 0]

# Request user input
_input = input("Beginning phrase:\n\t<< ")

# Make sure to treat user input as text-only, not a regex expression. For this we put "\" before any matched special character. :w
_input = re.sub(r"([\!\@\#\$\%\^\&\*\(\)\_\-\+\=\{\}\[\]\\\|\:\"\;\'\<\,\>\.\?\/])", r"\\\1", _input)

# We have to compile the input the user entered as a regular expression. We can't use the r"" shorthand
regular_expression = re.compile(_input)

# Check if there is a match
if(re.search(regular_expression, read_data)):
    # Store the beginning index of the match
    index[0] = re.search(regular_expression, read_data).start()

    # Request user input for a second time
    _input = input("End phrase:\n\t<< ")

    # Make sure to treat user input as text-only again
    _input = re.sub(r"([\!\@\#\$\%\^\&\*\(\)\_\-\+\=\{\}\[\]\\\|\:\"\;\'\<\,\>\.\?\/])", r"\\\1", _input)

    # Compile the user input as a regular expression
    regular_expression = re.compile(_input)

    # Check if there is another match
    if(re.search(regular_expression, read_data)):
        # Store the end index of the match
        index[1] = re.search(regular_expression, read_data).end()

        # Print out the entire string the user is referring to
        print("\n" + "=== "*20 + "\n")
        print(read_data[index[0]:index[1]])
        print("\n" + "=== "*20 + "\n")
        
        _input = input("Is this your text?\n\t<< ")
        
        if _input.lower().strip().replace(" ", "") in ["yes", "y", "si", "s"]: 

            # Clear the clipboard before appending text to it
            tk_object.clipboard_clear()

            # Store the output to the user's clipboard
            tk_object.clipboard_append(read_data[index[0]:index[1]])

            # Make sure the text in the clipboard stays there even if the program is closed
            tk_object.update()

            # Print confirmation message
            print("Text successfully stored in clipboard!")

    else:
        # There was no match and the string was not found
        print("Text not found. Try again")

else:
    # There was no match and the string was not found
    print("Text not found. Try again")


# We're finished with the Tk object, so we must destroy it
tk_object.destroy()
