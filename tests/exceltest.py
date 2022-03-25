import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from excel2json import excel2json
from json2excel import json2excel


filename = 'apotek.xlsx'
url = 'https://legemiddelverket.no/Documents/Import%20og%20salg/Apotekdrift/Apotektillatelser/landets%20apotek%20.xlsx'

jsonstr = excel2json(url)
json2excel(jsonstr, 'newexcel.xlsx')