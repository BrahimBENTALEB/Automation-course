from openpyxl import load_workbook
from openpyxl.styles import Font

wb=load_workbook('report.xlsx')
sheet = wb['report']

sheet['E1']='Sales Report'
sheet['E2']='January'
sheet['E1'].font = Font('Arial',bold=True,size=20)
sheet['E2'].font = Font('Arial',bold=True,size=14)

wb.save('report_january.xlsx')