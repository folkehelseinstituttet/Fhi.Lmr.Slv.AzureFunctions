import pandas as pd

def html2json(htmlurl: str):
    data = pd.read_html(htmlurl)[0]
    data = data.fillna("")
    json_str = data.to_json(orient='records')
    return json_str
