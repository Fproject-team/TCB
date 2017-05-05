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
        sql = "SELECT `ticket_data`,`ticket_department` FROM `test_ticket` WHERE `company_name` = %s"
        cursor.execute(sql ,(name,))
        result = cursor.fetchall()
        for i in result:
            TrainData.data.append(i[0])
            TrainData.target.append(i[1])
    connection.close()
    return TrainData


