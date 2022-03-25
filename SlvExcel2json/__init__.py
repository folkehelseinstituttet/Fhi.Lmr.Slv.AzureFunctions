import logging

import azure.functions as func
from csv import excel
import pandas as pd
from excel2json import excel2json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('SLV-Excel2json Python HTTP trigger function processed a request.')

    url = req.params.get('url')
    if not url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('url')

    if url:
        return func.HttpResponse(excel2json(url))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a url to an Apotek xlsx in the query string or in the request body to convert to json.",
             status_code=200
        )
