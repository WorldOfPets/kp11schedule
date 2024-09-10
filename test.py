import pandas as pd
import numpy as np
import keyboard
import os
import time
from mainfunc import get_sheet_for_teacher

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
    clr()
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
                    #df = pd.read_excel("./excel/" + str(files[step]), sheet_name='чет')
                    print(type(np.random.randn(20, 6)))
                    #print(type(get_sheet_for_teacher("Поливанов")))
                    new_np_array = np.asarray(get_sheet_for_teacher("Поливанов"))
                    print(type(new_np_array))
                    print(new_np_array)
                    df = pd.DataFrame(np.rot90(new_np_array), columns=["понедельник", "вторник", "среда", "четверг", "пятница", "суббота"])
                    df.index += 1
                    print(df.to_string())
                    break
                else:
                    print("У файла неверный формат")
            else:
                exit() 
            
        clr()
        write_step_one(step)


if __name__ == '__main__':
    cli()