import pandas as pd

def html2json(htmlurl: str, jsonfilename: str):
    data = pd.read_html(htmlurl)
    json_str = data.to_json(path=None, orient='table')
    return json_str
