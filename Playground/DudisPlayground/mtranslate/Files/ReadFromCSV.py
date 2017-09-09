import csv

import Playground.DudisPlayground.mtranslate.DB.WriteToDB
from Playground.DudisPlayground.mtranslate import translate

DB = Playground.DudisPlayground.mtranslate.DB.WriteToDB
with open("C:\Users\dudia\Desktop\TCB\HarelDataSet\MiniHarelDB.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        title = translate(row['Title'].decode('windows-1255').encode('UTF-8'))
        description = translate(row['Description'].decode('windows-1255').encode('UTF-8'))
        department = translate(row['Department'].decode('windows-1255').encode('UTF-8'))
        ticket_data = title+ " " +description
        ticket_department = department
        DB.WriteToDB(ticket_data,ticket_department)
        print(title,description,department)
