
import keyboard
import os
import time

options = ["varian 1", "variant 2", "variant 2", "variant 2"]
# Указываем путь к директории
directory = "./excel"

# Получаем список файлов
files = os.listdir(directory)
files.append("Отмена")

def write_step_one(variant):
    print("Select variant:")
    for i in range(len(files)):
        if i == variant:
            print(f"> {files[i]} <")
        else:
            print(files[i])

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
        elif pressed_key == keyboard.KEY_DOWN and step < len(files)-1:
            step+=1
            time.sleep(0.13)
        elif pressed_key == "enter":
            if "." in files[step]:
                splfile = files[step].split(".")[-1]
                if "xls" in splfile:
                    continue
                else:
                    print("У файла неверный формат")
            else:
                exit() 
            
        clr()
        write_step_one(step)


if __name__ == '__main__':
    cli()