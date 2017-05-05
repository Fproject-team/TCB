from __future__ import print_function
import pymysql
def ReadFromDB(company_name):
    name = company_name
    class TrainData:
        data = []
        target = []
    connection = pymysql.connect(host='104.199.79.238', port=3306, user='root', passwd='123456', db='test')
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `classify` FROM `classifies` WHERE `comp_name` = %s"
        cursor.execute(sql ,(name,))
        result = cursor.fetchall()
    connection.close()
    return result
