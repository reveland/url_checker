import os
import ast
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Provider():

    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds_json = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
        creds_dict = ast.literal_eval(creds_json)
        creds = ServiceAccountCredentials.from_json_keyfile_dict(
            creds_dict, scope)
        client = gspread.authorize(creds)

        sheet_key = os.environ['SHEET_KEY']
        document = client.open_by_key(sheet_key)
        self.sheet = document.worksheet('lista')

    def get_table(self):
        return self.sheet.get_all_records()
