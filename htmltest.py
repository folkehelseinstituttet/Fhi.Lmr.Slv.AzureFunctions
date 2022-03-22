from html2json import html2json
from json2html import json2thtml

jsonstr = html2json('http://fest.legemiddelverket.no/ApotekregisterWebApp/')
htmlstr = json2thtml(jsonstr)
print(htmlstr)