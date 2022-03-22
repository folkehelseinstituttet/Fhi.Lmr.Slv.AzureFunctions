from csv import excel
import pandas as pd

def excel2json(xlsxfilename: str, jsonfilename: str):
    data = pd.read_excel(xlsxfilename, header=2)
    data.to_json(jsonfilename, orient='table')

    