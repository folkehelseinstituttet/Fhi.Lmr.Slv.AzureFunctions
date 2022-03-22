import pandas as pd

def html2json(htmlurl: str, jsonfilename: str):
    data = pd.read_html(htmlurl)
    data.to_json(jsonfilename, orient='table')

