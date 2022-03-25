from csv import excel
import pandas as pd

def excel2json(xlsxfilename: str):
    '''Function to convert an excel file to json.
    the argument xlsxfilename takes either a file, path or url.
    Returns a string with the json text'''
    
    data = pd.read_excel(xlsxfilename, header=2)
    data = data.fillna("")
    json_str = data.to_json(orient='records')
    return json_str

