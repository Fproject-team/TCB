import csv
from mtranslate import translate

with open("C:\Users\dudia\Desktop\TCB\HarelDataSet\HarelDataCRM.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        title = translate(row['Title'].decode('windows-1255').encode('UTF-8'))
        description = translate(row['Description'].decode('windows-1255').encode('UTF-8'))
        department = translate(row['Department'].decode('windows-1255').encode('UTF-8'))
        print(title,description,department)
