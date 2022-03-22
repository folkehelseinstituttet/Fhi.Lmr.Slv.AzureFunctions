import pandas as pd
from datetime import datetime

def json2excel(jsonfilename: str, xlsxfilename: str):
    data_new = pd.read_json(jsonfilename, orient='table')

    text1='Landets Apotek'
    text2=datetime.now().strftime("%d/%m/%Y")

    writer = pd.ExcelWriter(xlsxfilename)
    data_new.to_excel(writer, startrow=2, startcol=0, index=False)

    worksheet=writer.sheets['Sheet1']
    worksheet.write(0,0,text1)
    worksheet.write(1,0,text2)
    writer.save()