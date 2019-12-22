import keyboard
import time
import random


def access_portal():
    keyboard.press_and_release("win+r")
    time.sleep(0.1)
    write_command("cmd\n", 0.5, 0)
    write_command("ssh estudiante@rumad.uprm.edu\n", 0, 0)
    keyboard.wait('enter')
    time.sleep(1)
    

def write_command(message, sleep=0.5, interval=None):
    if interval == None:
        interval = 0.15/random.randint(1,3)
    for char in str(message):
        keyboard.write(str(char), exact=True)
        time.sleep(float(interval))
    time.sleep(float(sleep))


def main():
    access_portal()
    write_command(5, 0.1)
    write_command(6, 0.1)
    write_command(3, 0.1)


if __name__=="__main__":
    time.sleep(1)
    main()
