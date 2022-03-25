import pandas as pd

def html2json(htmlurl: str):
    '''Function to convert html to json.
    The argument htmlurl takes a url.
    Returns a string with the json text'''
    data = pd.read_html(htmlurl)[0]
    data = data.fillna("")
    json_str = data.to_json(orient='records')
    return json_str
