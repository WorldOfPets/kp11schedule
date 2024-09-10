
from mainfunc import *


def main():
    for less in get_lesson():
        print(less)
    print(list(get_teachers()))
    print(get_cabinets())
    print(get_groups())
    # start = str(input("Что ты хочешь сделать?\n1.Получить расписание для преподавателя\n2.Получить расписание для группы"))
    # valsearch = "example"
    # if start == "1":
    #     valsearch = str(input("Teacher name:"))
    #     add_event(get_lesson_for_teacher(valsearch, "среда"))
    # elif start == "2":
    #     valsearch = str(input("Group name:"))
    #     add_event(get_lesson_for_group(valsearch))
    # with open(f'{valsearch}.ics', 'wb') as file:
    #     file.write(calendar.to_ical())

if __name__ == "__main__":
    main()


# Запись календаря в файл
