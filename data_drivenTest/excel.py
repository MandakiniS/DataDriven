import pandas as pd

file_path = "/Users/smandaki/PycharmProjects/DataDriven/data/TestData.xlsx"

sheetsInEx= pd.ExcelFile(file_path)
print(sheetsInEx.sheet_names)
sheetCount= len(sheetsInEx.sheet_names)
print(sheetCount)

for sheet in sheetsInEx.sheet_names:
    print(sheet)

