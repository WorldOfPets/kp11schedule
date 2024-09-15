
from mainfunc import *


def main():
    # for less in get_lesson():
    #     print(less)
    # print(list(get_teachers()))
    # print(get_cabinets())
    # print(get_groups())
    start = str(input("Что ты хочешь сделать?\n1.Получить расписание для преподавателя\n2.Получить расписание для группы"))
    valsearch = "example"
    if start == "1":
        #valsearch = str(input("Teacher name:"))
        tech = get_teachers()
        print(set(tech))
        # for i in set(tech):
        #     add_event(get_lesson_for_teacher(i, "среда"), i, False, True)
        
        add_event_group(get_lesson_for_group("ИСиП-35 (11кл)"), "ИСиП35", False)
            
    elif start == "2":
        valsearch = str(input("Group name:"))
        add_event(get_lesson_for_group(valsearch))
    elif start == "3":
        print(check_right_format())
    # with open(f'{valsearch}.ics', 'wb') as file:
    #     file.write(calendar.to_ical())

if __name__ == "__main__":
    main()


# Запись календаря в файл
