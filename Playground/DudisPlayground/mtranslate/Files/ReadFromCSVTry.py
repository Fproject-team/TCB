import csv
import sys

import DudisPlayground.mtranslate.Classify.DB.DBOrganize
from Playground.DudisPlayground.mtranslate.Classify.Translate.core import translate

DB = DudisPlayground.mtranslate.Classify.DB.DBOrganize
def ReadFromCSV(path,comp_name):
    csvpath = path
    comp = comp_name
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                title = translate(row['Title'].decode('windows-1255').encode('UTF-8'))
                description = translate(row['Description'].decode('windows-1255').encode('UTF-8'))
                department = translate(row['Department'].decode('windows-1255').encode('UTF-8'))
                ticket_data = title+ " " +description
                ticket_department = department
                DB.WriteToDB(ticket_data,ticket_department,comp)
            except Exception:
                sys.exc_clear()
