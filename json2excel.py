import pandas as pd
from datetime import datetime

def json2excel(jsonstr: str, xlsxfilename: str):
    data_new = pd.read_json(jsonstr, orient='records')

    text1='Landets Apotek'
    date=datetime.now().strftime("%d.%m.%Y")
    text2='Oversikt oppdatert: ' + date

    writer = pd.ExcelWriter(xlsxfilename)
    data_new.to_excel(writer, startrow=2, startcol=0, index=False)

    worksheet=writer.sheets['Sheet1']
    worksheet.write(0,0,text1)
    worksheet.write(1,0,text2)
    writer.save()