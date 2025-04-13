import openpyxl
import os

def get_login_data(filename):

    # Dynamically get the full path to the Excel file
    base_dir = os.path.dirname(os.path.abspath(__file__))  # path to utils folder
    file_path = os.path.join(base_dir, '..', 'test_data', filename)
    file_path = os.path.normpath(file_path)  # Normalize for OS compatibility

    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append((row[5], row[6]))  # username, password
    return data

