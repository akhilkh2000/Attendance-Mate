import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import  pprint
from datetime import date

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)



sheet = client.open("Attendance").sheet1

#
# row = sheet.row_values(2)
# col = sheet.col_values(3)
# cell = sheet.cell(1,2).value
# insertRow = [4 ,"abhi",50]
# sheet.insert_row(insertRow,3)
# sheet.update_cell(2,2,"changed")
# numRows = sheet.row_count;

# pprint(data)
today = str(date.today())
data = sheet.get_all_records()

# print(row)
# print(cell_list)

sheet.add_cols(1)
# print(data)
# print(len(data[0]))

currColCount = len(data[0])
newColNo=currColCount+1
totalColNo=sheet.find('total').col
sheet.update_cell(1, newColNo, today)
rolls = [1, 2, 3, 4]
present_rolls = [1,2,3]
row=0
for roll in rolls:

    cell_list = sheet.findall(str(roll))
    for cell in cell_list:
        if cell.col:
            row = cell.row
            total = int(sheet.cell(row, totalColNo).value)
            total = total + 1
            sheet.update_cell(row, totalColNo, str(total))
    #     do error handling here

    if roll not in present_rolls:
        present = False
    else:
        present = True
    if present:

        presentCol = sheet.find('totalPresent').col
        value = int(sheet.cell(row, presentCol).value)
        print("present"+str(value))
        value = value + 1;
        sheet.update_cell(row, presentCol, str(value))
        sheet.update_cell(row, newColNo ,'P')
    else:

        absentCol = sheet.find('totalAbsent').col
        value = int(sheet.cell(row, absentCol).value)
        print("absent" + str(value))
        value = value + 1;
        sheet.update_cell(row, absentCol, str(value))
        sheet.update_cell(row, newColNo, 'A')
#

