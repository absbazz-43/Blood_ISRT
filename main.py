import gspread
from oauth2client.service_account import ServiceAccountCredentials
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("file.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Blood").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

  # Get a specific row
fname= sheet.col_values(2)
fbatch = sheet.col_values(3)
fgroup = sheet.col_values(4)
fphone = sheet.col_values(5)

class Example(MDApp):
    def build(self):
        self.icon = "drop.png"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        layout = AnchorLayout()
        data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("Serial", dp(40)),
                ("Name", dp(40)),
                ("Batch", dp(40)),
                ("Blood Group", dp(40)),
                ("Phone", dp(40)),
            ],
            row_data=[(f"{i + 1}",fname[i], fbatch[i],fgroup[i],fphone[i]) for i in range(2,len(data)+1)],
        )
        layout.add_widget(data_tables)
        return layout


Example().run()








