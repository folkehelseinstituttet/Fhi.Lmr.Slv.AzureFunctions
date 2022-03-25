import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from html2json import html2json
from json2html import json2thtml

jsonstr = html2json('http://fest.legemiddelverket.no/ApotekregisterWebApp/')
htmlstr = json2thtml(jsonstr)
print(htmlstr)