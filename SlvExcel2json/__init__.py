import logging

import azure.functions as func
import pandas as pd
# from urllib.parse import quote

def excel2json(xlsxfilename: str):
    '''Function to convert an excel file to json.
    the argument xlsxfilename takes either a file, path or url.
    Returns a string with the json text'''
    logging.info('Inside excel2json')
    data = pd.read_excel(xlsxfilename, header=2)
    logging.info('Excel read')
    data = data.fillna("")
    json_str = data.to_json(orient='records')
    logging.info('Converted to json')
    return json_str

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('SLV-Excel2json Python HTTP trigger function processed a request.')
    
    urlraw = req.params.get('url')
    logging.info(urlraw)
    # url='https://legemiddelverket.no/Documents/Import%20og%20salg/Apotekdrift/Apotektillatelser/landets%20apotek%20.xlsx'
    if urlraw:    
        url = urlraw.replace(' ','%20')
        logging.info('Parameter is '+url)
        json = excel2json(url)
        return func.HttpResponse(json)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a url parameter to an Apotek xlsx in the query string to convert to json.",
             status_code=200
        )
