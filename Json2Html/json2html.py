import pandas as pd
import ast

def json2thtml(jsonstr: str):
    data = pd.read_json(jsonstr, orient='records')
    html_str = data.to_html()
    return html_str