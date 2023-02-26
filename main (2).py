import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\W.C\\Downloads\\blood\\file.json", scope)

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
                ("Name", dp(40)),
                ("Batch", dp(40)),
                ("Blood Group", dp(40)),
                ("Phone", dp(40)),
            ],
            row_data=[
                ('Md. Ariful Islam Sanim', '21', 'A+', '8801521449210'),
                 ('Tareq RahmanT', '24', 'A+', '8801729433663'),
                 ('Arman Mahmud', '25', 'A+', '8801516051655'),
                 ('Shaila sharmin deena', '19', 'A+', ' '),
                 ('Maisha Maliha Rahman', '23', 'A+', ' '),
                 ('Toolip', '23', 'A+', '8801914322535'),
                 ('Bushra', '21', 'A+', ' '),
                 ('Md. Ariful Islam Sanim', '21', 'A+', '8801521449210'),
                 ('prosanjit shaha', '24', 'A+', '8801635538344'),
                 ('Md Golam Mostofa.', '24', 'A+', '8801717327850'),
                 ('Rony', '24', 'A+', '8801521508553'),
                 ('Amol Saha', '24', 'A+', ' '),
                 ('MD. Tarikul Hasan', '15', 'A+', '8801675824795'),
                 ('Suraiya parven mukta', '18', 'A+', '8801521332004'),
                 ('Polock Biswas', '24', 'A+', '8801817518325'),
                 ('Niamul', '19', 'AB-', '8801919086522'),
                 ('Md.Emran Hosen', '24', 'AB-', '8801316464549'),
                 ('Tarikul Islam', '24', 'AB+', ' '),
                 ('Akash', '24', 'AB+', '8801784651364'),
                 ('Minhaz', '21', 'AB+', '8801750645755'),
                 ('Oishe', '23', 'AB+', ' '),
                 ('Priom Saha', '23', 'AB+', '8801521416559'),
                 ('salauddin', '23', 'AB+', ' '),
                 ('Joy', '24', 'AB+', ' '),
                 ('Foysal Ahmed', '24', 'AB+', ' '),
                 ('Akash deb', '24', 'AB+', '8801784651364'),
                 ('Farhan Taohid', '24', 'B-', ' '),
                 ('Humaira Sultana Hridita', '24', 'B+', ' '),
                 ('Mahnaz', '24', 'B+', ' '),
                 ('Eraf Hossain', '24', 'B+', '8801941202104'),
                 ('Sanaul Islam Nishat', '23', 'B+', '8801722526119'),
                 ('MD. ABDULLAH AL NOMAN', '22', 'B+', '8801689305051'),
                 ('Dipu Ray', '24', 'B+', '8801789645378'),
                 ('Tanvir Md Sarwer Sabbir', '23', 'B+', '8801730200561'),
                 ('Prianka Barman', '23', 'B+', '8801795187544'),
                 ('Zenia', '21', 'B+', ' '),
                 ('Mohirul', '23', 'B+', ' '),
                 ('Md. Mahabubur Rahman', '21', 'B+', '8801687050977'),
                 ('Md. Faisal Ahamed Seyam', '21', 'B+', '8801884691644'),
                 ('Md. Aminul Islam Farhad', '22', 'B+', '8801521326850'),
                 ('Nofel Ahmed', '23', 'B+', '8801776683145'),
                 ('Md.Al-Amin Islam', '24', 'B+', '8801726297382'),
                 ('Asnan', '24', 'B+', '8801521545005'),
                 ('Ishtiaq ishrak', '24', 'B+', '8801521528474'),
                 ('Md:Monoarul Islam', '24', 'B+', '8801722343945'),
                 ('Md Rakib Hossen', '24', 'B+', '8801627343464'),
                 ('Sakib', '24', 'B+', '8801781090493'),
                 ('Md. Moinuzzaman Romel', '14', 'B+', ' '),
                 ('Monoarul', '24', 'B+', '8801722343945'),
                 ('abu hanifa', '25', 'B+', '8801521565510'),
                 ('Mohammad Ariful Hasan', '16', 'B+', '8801708146951'),
                 ('Mohammad Ariful Hasan', '16', 'B+', '8801708146951'),
                 ('mosiur', '24', 'B+', '8801716767288'),
                 ('Saddam Hossain Irfan', '19', 'B+', ' '),
                 ('Utpaul Chandra Debsharma', '22', 'B+', '8801521302867'),
                 ('goat', '23', 'B+', ' '),
                 ('Ayshwaria Saha', '24', 'O-', '8801558459180'),
                 ('NABIL AHMED UTHSO', '24', 'O+', '8801642368908'),
                 ('Shafayet khan shafee', '24', 'O+', '8801791051104'),
                 ('Al Imran Preyo', '19', 'O+', '8801719057059'),
                 ('Sabbir Ahmed Hemo', '21', 'O+', '8801738047781'),
                 ('Md Shawon Badsha', '22', 'O+', '8801521432510'),
                 ('Sazid abdullah', '23', 'O+', ' '),
                 ('NIAMUL', '24', 'O+', '8801919086522'),
                 ('Mohasina Rahaman', '24', 'O+', ' '),
                 ('shahriar ayon', '25', 'O+', '8801624791886'),
                 ('Anindita Saha', '23', 'O+', ' '),
                 ('Zubair', '20', 'O+', '8801521208108'),
                 ('Rubaiya', '21', 'O+', '8801866032441'),
                 ('Rasel', '20', 'O+', '8801723768606'),
                 ('Tasnim', '23', 'O+', '8801788365235'),
                 ('Md.Mohsinur Rahman', '24', 'O+', '8801751474459'),
                 ('Hridoy Patwary', '24', 'O+', '8801956777731'),
                 ('Mohasina Rahaman', '24', 'O+', ' '),
                 ('Mohasina Rahaman', '24', 'O+', ' '),
                 ('Abul Bashar Sudip', '24', 'O+', ' '),
                 ('Tasnim Ara', '21', 'O+', '8801771772522'),
                 ('nowshin jahan', '24', 'O+', ' '),
                 ('Mahmudul hassan riad', '24', 'O+', '8801631340037'),
                 ('Ziaul Haque', '24', 'O+', '8801308740205'),
                 ('Bashir Ahmed', '24', 'O+', '8801793997119'),
                 ('Palash', '24', 'O+', ' '),
                 ('Tarannum Bente Sohrab Mumu', '23', 'O+', ' '),
                 ('Mahabub Hasan Emon', '20', 'O+', '8801515678958'),
                 ('Syed Mejbahul Alam', '19', 'O+', '8801770877508'),
                 ('UTTAM KUMAR RAY', '23', 'O+', '8801738387386'),
                 ('Rudra', '25', 'O+', '8801629976764'),
                 ('Miraz Hossain', '21', 'O+', ' '),
                 ('Khondoker Shahriar Islam Ayon', '25', 'O+', '8801624791886'),
                 ('Md sohel Miah', '20', 'O+', '8801750999557'),
                 ('swapnil roy', '23', 'O+', '8801753848191'),
                 ('Sabbir Ahmed Hemo', '21', 'O+', '8801738047781'),
                 ('Asma ul hosna', '24', 'O+', '8801534282666'),
                 ('Fahim Ahmed Shaensha', '26', 'A+', '8801641830385'),
                 ('Maliha Siddika', '26', 'O+', '8801313942813'),
                 ('sahib al kawsar', '26', 'O+', '8801944176101'),
                 ('Nahian Nujhat', '26', 'O+', '8801990225488'),
                 ('Aman Ullah Aman', '26', 'B+', '8801308498404'),
                 ('Nadia Afrin', '26', 'B+', '8801892816306'),
                 ('Anika Bushra', '26', 'O+', '8801970089608'),
                 ('Mohammad Shadid Hossain', '26', 'B+', '8801776785546'),
                 ('Osama Bin Tahir', '26', 'B*', '8801928122844'),
                 ('Ruhan e elahi', '26', 'O+', '8801641097473'),
                 ('Tayaba chragee prachee', '26', 'O+', '8801796200306'),
                 ('Taseen Junnat seen', '26', 'A+', '8801303901518'),
                 ('Tanjida Sharmin Meghla', '26', 'B+', '8801307955064'),
                 ('Afroza Akter Lima', '26', 'B+', '8801787570147'),
                 ('Mushfiqur Rahaman Iffat', '26', 'A+', '8801798514859'),
                 ('Saraf Nawer Chowdhury', '26', 'B+', '8801953783871'),
                 ('Md. Al amin', '26', 'A+', '8801521756623'),
                 ('Ferdous Hasan Fahim', '26', 'O+', '8801517830675'),
                 ('Md. Ibrahim All-Mamun', '26', 'O+', '8801776957970'),
                 ('Faria Rauf Ria', '26', 'B+', '8801788755779'),
                 ('Md. Monayer Kabir Chowdhury', '26', 'B+', '8801717403021'),
                 ('Dev Kumar Sarkar', '26', 'O+', '8801706984122'),
                 ('SYED NADID ELHAM', '26', 'B+', '8801711347276'),
                 ('Sanjida Alam', '26', 'A+', '8801843837154'),
                 ('Mst. Mariam', '26', 'O+', '8801758691532'),
                 ('Muhammad Mutasim', '26', 'O+', '8801799587786'),
                 ('Siam Hossain', '26', 'B+', '8801610262233'),
                 ('Zarif Moen Raiyen', '26', 'A+', '8801316560770'),
                 ('Mejanur Rahman Sourav', '26', 'O+', '8801765404286'),
                 ('Saikat Ahmmed', '26', 'A+', '8801781787162'),
                 ('Shara Marjan', '26', 'B+', '8801521743969'),
                 ('Dabirul isalm', '26', 'B+', '8801704377532'),
                 ('MD.Nayemur Rahman', '26', 'O+', '8801517848632'),
                 ('Muhtasimul Haque', '26', 'O+', '8801787173353'),
                 ('Md Badhon Islam', '26', 'A+', '8801786745775'),
                 ('Jannatul yasmin', '26', 'O+', '8801733570083'),
                 ('Suave kamal', '26', 'O+', '8801871565352'),
                 ('Faria Sharmin', '26', 'O+', '8801973032932'),
                 ('Abrar Sakib Zihad', '26', 'O+', '8801707035214'),
                 ('Md. Arman Hossain Turag', '26', 'B+', '8801624852895'),
                 ('Sudipto Kumar Saha', '26', 'B+', '8801536194075'),
                 ('Md Hasibul Islam Jitu', '26', 'A+', '8801902878420'),
                 ('Mishkat Mahiuddin', '26', 'A+', '8801779712362'),
                 ('Mir Mashrafi Alam', '26', 'O+', '8801855415620'),
                 ('Bushra Chowdhury', '26', 'A+', '8801711305792'),
                 ('Raisa Rashid Mim', '26', 'B+', '8801839806343'),
                 ('Refayat Jamal', '26', 'A+', '8801771380689'),
                 ('Shafin Ahmed', '26', 'A+', '8801786584383'),
                 ('Farhana Rokaiya Ramiza', '26', 'A+', '8801744999459'),
                 ('Maliha Binte Alauddin', '26', 'B+', '8801760079028'),
                      ],
        )
        layout.add_widget(data_tables)
        return layout


Example().run()








