import openpyxl
import sys
def test_run(filePath):
    wb = openpyxl.load_workbook(filePath)

    ws = wb.active

    for row in ws.iter_rows(min_row=4, max_row=4):
        for cell in row:
            if cell.value is not None:
                print(cell.value)

def main():
    # Получаем путь к файлу из аргумента командной строки
    if sys.argv is not None and len(sys.argv) > 1:
        filePath = sys.argv[1]
        test_run(filePath)

if __name__ == '__main__':
    main()

x = input()