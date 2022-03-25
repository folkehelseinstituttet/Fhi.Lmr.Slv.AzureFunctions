from excel2json import excel2json
from json2excel import json2excel

jsonstr = excel2json('apotek.xlsx')
json2excel(jsonstr, 'newexcel.xlsx')