import openpyxl
import sys
from basedef import get_lesson, get_cabinets, get_day, get_lesson_num
from openpyxl.styles import PatternFill


days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота"]

def find_cabinet(filePath, row_id):
    wb = openpyxl.load_workbook(filePath, read_only=False, keep_vba=True)

    ws = wb.active
    lessons = get_lesson(ws)

    cabinets = get_cabinets(ws)
    day = get_day(ws, 1, int(row_id))
    less_num = get_lesson_num(ws, 2, int(row_id))
    # str(input("Для поиска кабинета укажите день недели и номер урока\nПример: 1 7 или понедельник 1\nЖду: ")).split(" ")
    # if len(day) < 3:
    #     day = days[day-1]
    for less in lessons:
        if less.lesson_day == day and str(less.lesson_num) == str(less_num):
            if less.cabinet in cabinets[0]:
                try:
                    cabinets[0].remove(less.cabinet)
                except Exception as ex:
                    print(".", end="")
    print(f"Вот список свободных кабинетов на {day} на {less_num} урок:")
    print(cabinets[0])
    print("ОШИБКИ В НАЗВАНИИ КАБИНЕТОВ: Исправьте их для более точно поиска кабинета")
    print(cabinets[1])
    for i in cabinets[1]:
        ws[f"{ws[i].coordinate}"].fill = PatternFill(patternType='solid', fgColor='FF3300')
    
    wb.save(str(filePath))




def main():
    # Получаем путь к файлу из аргумента командной строки
    if sys.argv is not None and len(sys.argv) > 1:
        filePath = sys.argv[1]
        find_cabinet(filePath, sys.argv[2])

if __name__ == '__main__':
    #try:
        main()
    # except Exception as ex:
    #     print(ex)
    #     x = input()
x = input()