import csv
import sys
import chardet
from Playground.DudisPlayground.mtranslate import translate
import Playground.DudisPlayground.mtranslate.DBOrganize
DB = Playground.DudisPlayground.mtranslate.DBOrganize
with open("C:\Users\dudia\Desktop\TCB\HarelDataSet\NewHarel.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            title = translate(row['Title'].decode('windows-1255').encode('UTF-8'))
            description = translate(row['Description'].decode('windows-1255').encode('UTF-8'))
            department = translate(row['Department'].decode('windows-1255').encode('UTF-8'))
            ticket_data = title+ " " +description
            ticket_department = department
            DB.WriteToDB(ticket_data,ticket_department)
        except Exception:
            sys.exc_clear()
