from __future__ import print_function
import pymysql
connection = pymysql.connect(host='104.199.79.238', port=3306, user='root', passwd='123456', db='test')
with connection.cursor() as cursor:
    # Read a single record
    sql = "SELECT `*` FROM `test_ticket`"
    cursor.execute(sql)
    '''
    sql = "SELECT `id`, `Name` FROM `TestTable` WHERE `Phone`=%s"
    cursor.execute(sql, ('050'))
    '''
    result = cursor.fetchall()
    print(result)

connection.close()