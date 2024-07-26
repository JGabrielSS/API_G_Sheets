import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_file("../Cloud_Credentials/api-sheets-credential.json",scopes=SCOPES)
client = gspread.authorize(creds)

sheets_id = "1xBmF8HmZKdES8q3kalwOdPQ1G2TIR_XyHypBIruVu7M"
workbook = client.open_by_key(sheets_id)


