import pandas as pd
import numpy as np
import keyboard
import os
import time
from mainfunc import get_sheet_for_teacher
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

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
                    df = pd.DataFrame(np.rot90(new_np_array), columns=["Поливанов", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота"])
                    df.index += 1
                    #df = pd.DataFrame(np.random.random((10, 3)), columns=("col 1", "col 2", "col 3"))

                    # Преобразуем DataFrame в таблицу
                    fig, ax = plt.subplots(figsize=(12, 4))
                    ax.axis('tight')
                    ax.axis('off')
                    the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')

                    # Сохраняем PDF файл
                    pp = PdfPages("foo.pdf")
                    pp.savefig(fig, bbox_inches='tight')
                    pp.close()
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