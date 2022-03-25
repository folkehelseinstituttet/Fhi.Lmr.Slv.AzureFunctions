import pandas as pd
import ast

def json2thtml(jsonstr: str):
    '''Converts json text to html text.
    Takes in a json string and returns a html string.'''
    
    data = pd.read_json(jsonstr, orient='records')
    html_str = data.to_html()
    return html_str