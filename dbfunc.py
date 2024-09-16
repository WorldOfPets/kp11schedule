import sqlite3
import openpyxl
from sql_script import create_table
from basedef import get_unic_lesson

DB = 'C:\\Users\\Admin\\Desktop\\testPYVBA\\main.sqlite3'

#wb = openpyxl.load_workbook("rasp.xlsx", read_only=False, keep_vba=True)
#ws = wb.active

def create_tables():
    # Список SQL-выражений для создания таблиц
    sql_statements = create_table
    try:
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)
            conn.commit()
    except sqlite3.Error as e:
        print(e)

def find_less(lesson):
    less = str(lesson).replace("(1 п", "").replace("(2 п", "").replace("( 2 п", "").replace("( 1 п", "").strip()
    sql = f"""
    SELECT * FROM lesson
    WHERE name LIKE '%{less}%';
    """
    try:
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            data = cursor.execute(sql).fetchall()
            print(len(data))
            conn.commit()
            return len(data)
    except sqlite3.Error as e:
        print(e)

def find_cabinet(cabinet):
    cab = str(cabinet).strip()
    sql = f"""
    SELECT * FROM cabinets
    WHERE name='{cab}';
    """
    try:
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            data = cursor.execute(sql).fetchall()
            print(len(data))
            conn.commit()
            return len(data)
    except sqlite3.Error as e:
        print(e)

def find_teacher(teacher):
    tech = str(teacher).strip()
    print(tech)
    sql = f"""
    SELECT * FROM teachers
    WHERE fio='{tech}';
    """
    try:
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            data = cursor.execute(sql).fetchall()
            print(len(data))
            conn.commit()
            return len(data)
    except sqlite3.Error as e:
        print(e)
# if __name__ == '__main__':
#     #create_tables()
#     #add_cabinets()
#     find_teacher("Колосова Е.Б.")