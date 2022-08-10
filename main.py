import openpyxl

#path = 'C:\\Users\\kramk\\PycharmProjects\\selenium\\Book.xlsx'
workbook = openpyxl.load_workbook('Book.xlsx')
sheet = workbook.active


for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(rows=r, columns=c).value = "welcome"
sheet.save(path)

