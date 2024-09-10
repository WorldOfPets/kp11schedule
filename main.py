import openpyxl
import icalendar
import pytz
from dateutil.rrule import rrule, WEEKLY
from datetime import datetime, timedelta

from typing import List

wb = openpyxl.load_workbook(str(input("Path to excel file: ")))

ws = wb.active

groups = []
days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота"]
lessons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
lessons_arr = []

class LessonKP11():
    teacher = ""
    cabinet = ""
    lesson_num = ""
    group = ""
    lesson_name = ""
    lesson_day = ""

    def __str__(self) -> str:
        return f"{self.teacher} {self.cabinet} {self.lesson_num} {self.group} {self.lesson_name} {self.lesson_day}"

def get_group(row_id, col_id):
    for row in ws.iter_rows(min_row=row_id, max_row=row_id):
        for cell in row:
            if cell.value is not None and cell.column == col_id:
                return cell.value



def get_day(col_id, row_id):
    new_days = []
    for col in ws.iter_cols(min_col=col_id, max_col=col_id, max_row=row_id):
        for cell in col:
            if cell.value is not None and cell.value in days:
                #print(cell.value)
                new_days.append(cell.value)
    return new_days[-1] if new_days is not None else "понедельник"

def get_lesson_num(col_id, row_id):
    for col in ws.iter_cols(min_col=col_id, max_col=col_id, max_row=row_id, min_row=row_id-1):
        for cell in col:
            if cell.value is not None and cell.value in range(1, 11):
                return cell.value

def get_lesson() -> List[LessonKP11]:
    for row in ws.iter_rows():
        for cell in row:
            if cell.value is not None and "/" in str(cell.value) or str(cell.value) == "Разговоры о важном":
                if cell.offset(0, 1).value is not None:
                    lesson = LessonKP11()
                    lesson.cabinet = cell.offset(0, 1).value
                    lesson.group = get_group(4, cell.column)
                    lesson.lesson_day = get_day(1, cell.row)
                    if "п/гр" in str(cell.value):
                        new_cell_value = str(cell.value).replace("п/гр", "")
                        lesson.teacher = str(new_cell_value).split("/")[1] if "/" in str(cell.value) else "Куратор группы"
                    else:
                        lesson.teacher = str(cell.value).split("/")[1] if "/" in str(cell.value) else "Куратор группы"
                    lesson.lesson_num = get_lesson_num(2, cell.row)
                    lesson.lesson_name = str(cell.value).split("/")[0] if "/" in str(cell.value) else cell.value
                    lessons_arr.append(lesson)
    return lessons_arr

def get_lesson_for_teacher(teacher, day) -> List[LessonKP11]:
    list_less_t = []
    for less in get_lesson():
        if teacher in less.teacher:
            #print(less)
            list_less_t.append(less)
    return list_less_t
def get_lesson_for_group(group) -> List[LessonKP11]:
    list_less_g = []
    for less in get_lesson():
        if group in less.group:
            list_less_g.append(less)
    return list_less_g
#print(get_group(4, 3))
#print(get_day(1, 55))
#print(get_lesson_num(2, 48))
#get_lesson_for_teacher("Ковалева", "четверг")



# # Создание объекта Event

calendar = icalendar.Calendar()
def add_event(less_arr:List[LessonKP11]):
    print(len(less_arr))
    for less in less_arr:
        #print(less)
        print(less)
        this_wkst = days.index(less.lesson_day)
        #print(this_wkst)
        dstart = ""
        if less.lesson_num == 1:
            dstart = datetime(2024, 9, 2 + 7, 9, 0, 0, tzinfo=pytz.timezone('Europe/Moscow'))
        if less.lesson_num == 2:
            dstart = datetime(2024, 9, 2 + 7, 9, 55, 0, tzinfo=pytz.timezone('Europe/Moscow'))
        if less.lesson_num == 3:
            dstart = datetime(2024, 9, 2 + 7, 11, 0, 0, tzinfo=pytz.timezone('Europe/Moscow'))
        if less.lesson_num == 4:
            dstart = datetime(2024, 9, 2 + 7, 11, 55, 0, tzinfo=pytz.timezone('Europe/Moscow'))
        if less.lesson_num == 5:
            dstart = datetime(2024, 9, 2 + 7, 13, 00, 0, tzinfo=pytz.timezone('Europe/Moscow'))
        if less.lesson_num == 6:
            dstart = datetime(2024, 9, 2 + 7, 13, 55, 0, tzinfo=pytz.timezone('Europe/Moscow'))
        if less.lesson_num == 7:
            dstart = datetime(2024, 9, 2 + 7, 15, 00, 0, tzinfo=pytz.timezone('Europe/Moscow'))
        if less.lesson_num == 8:
            dstart = datetime(2024, 9, 2 + 7, 15, 55, 0, tzinfo=pytz.timezone('Europe/Moscow'))
        if less.lesson_num == 9:
            dstart = datetime(2024, 9, 2 + 7, 16, 50, 0, tzinfo=pytz.timezone('Europe/Moscow'))
        if less.lesson_num == 10:
            dstart = datetime(2024, 9, 2 + 7, 17, 45, 0, tzinfo=pytz.timezone('Europe/Moscow'))
        dstart += timedelta(days=this_wkst)
        dend = datetime(2024, 12, 31, 7, 0, 0, tzinfo=pytz.timezone('Europe/Moscow'))
        listDate = list(rrule(freq=WEEKLY, 
                             interval=2, 
                             until=dend,
                             dtstart=dstart))
        #print(len(listDate))
        for dateCurrent in listDate:
            event = icalendar.Event()
            event.add('summary', f"{less.lesson_name}/{less.cabinet}/{less.group}")
            event.add('location', f"{less.cabinet}")
            event.add('dtstart', dateCurrent)
            event.add('dtend', dateCurrent + timedelta(minutes=45))
            event.add('class', 'private')
            calendar.add_component(event)

# Добавление события в календарь

def main():
    start = str(input("Что ты хочешь сделать?\n1.Получить расписание для преподавателя\n2.Получить расписание для группы"))
    valsearch = "example"
    if start == "1":
        valsearch = str(input("Teacher name:"))
        add_event(get_lesson_for_teacher(valsearch, "среда"))
    elif start == "2":
        valsearch = str(input("Group name:"))
        add_event(get_lesson_for_group(valsearch))
    with open(f'{valsearch}.ics', 'wb') as file:
        file.write(calendar.to_ical())

if __name__ == "__main__":
    main()


# Запись календаря в файл
