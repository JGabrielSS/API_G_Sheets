import gspread
from google.oauth2.service_account import Credentials

# Defines the scope of the connection
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

# Pass and authorize the credential
creds = Credentials.from_service_account_file("../Cloud_Credentials/api-sheets-credential.json",scopes=SCOPES)
client = gspread.authorize(creds)

# Connects with spreadsheet using its id
sheets_id = "1xBmF8HmZKdES8q3kalwOdPQ1G2TIR_XyHypBIruVu7M"
workbook = client.open_by_key(sheets_id)

# Selecting active worksheet
worksheet = workbook.worksheet("Main")

# Getting spreadsheet title
work_sheet_title = workbook.worksheets()
print(work_sheet_title)

# Updating a cell
sheet_cell = worksheet.update_cell(2, 2, "Kobe")
print(worksheet.cell(2, 2).value)

# Updating active worksheet title
#worksheet.update_title("Main")

# Updating active worksheet cell content
worksheet.update_cell(5, 2, "August")
worksheet.update_acell("B4", "August")

#Locating a cell by value or position
value = worksheet.acell("B2").value
print(value)
value = worksheet.find("Watson")
print(value.row, value.col, "or", value)

# Basic formatting a cell
worksheet.format("A1:B13", {"horizontalAlignment" : "LEFT"})