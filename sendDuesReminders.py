# usr/bin/ env python3
# sendDuesReminders.py This program sends sendDuesReminders

import openpyxl, smtplib, sys

# Open spreadsheet and get the latest dues status
wb = openpyxl.load_workbook('duesRecords,xlsx')
sheet = wb.get_sheet_by_name('sheet1')

lastCol = sheet.get_highest_column()
latestMonth = sheet.cell(row=1, column=lastCol).value
