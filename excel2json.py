from csv import excel
import pandas as pd

def excel2json(xlsxfilename: str):
    data = pd.read_excel(xlsxfilename, header=2)
    data = data.fillna("")
    json_str = data.to_json(path=None, orient='records')
    return json_str

