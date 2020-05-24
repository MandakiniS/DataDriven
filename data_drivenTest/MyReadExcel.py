import pandas as pd

filename="/Users/smandaki/PycharmProjects/DataDriven/data/TestData.xlsx"
worksheet=pd.read_excel(filename,sheet_name='Login')

print(worksheet.shape)
'''value=worksheet['UserName']
print(value)'''


print(worksheet.loc['TestCaseID', 'UserName', 'Password '])






file_name = "/Users/smandaki/PycharmProjects/DataDriven/data/TestData.xlsx"
workbook1 = pd.read_excel(file_name, sheet_name=0)
column_values=workbook1['UserName']
print(column_values)
workbook2=pd.read_excel(file_name,sheet_name='configuration')
num1 = workbook1.shape
print(num1)
num2 = workbook2.shape
print(num2)

file_name="/Users/smandaki/PycharmProjects/DataDriven/data/TestData.xlsx"

files=pd.ExcelFile(file_name)
#print(files.sheet_names)
sheets = files.sheet_names
for sheet in sheets:
    print("Sheet names", sheet)
# just provided index col
newFile = pd.read_excel(file_name, sheet_name='Login')
print(newFile.shape)

#read reuired one column
print(newFile['Expected_result'])

#read the multiple colums
print(newFile[['Expected_result']])



# just provided index col
newFile1 = pd.read_excel(file_name, sheet_name='Login', index_col = 'Result')
print(newFile1.shape)

#read reuired one column
print(newFile1['Expected_result'])

#read required multiple column
print(newFile1[['Expected_result','UserName']])



