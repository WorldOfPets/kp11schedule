import curses
import keyboard
import os
import time

options = ["varian 1", "variant 2", "variant 2", "variant 2"]

def write_step_one(variant):
    print("Select variant:")
    for i in range(len(options)):
        if i == variant:
            print(f"> {options[i]} <")
        else:
            print(options[i])

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def cli():
    step = 0
    write_step_one(step)
    while True:
        pressed_key = keyboard.read_key()
        if pressed_key == keyboard.KEY_UP and step > 0:
            step-=1
            time.sleep(0.13)
        elif pressed_key == keyboard.KEY_DOWN and step < len(options)-1:
            step+=1
            time.sleep(0.13)
        clr()
        write_step_one(step)


if __name__ == '__main__':
    cli()