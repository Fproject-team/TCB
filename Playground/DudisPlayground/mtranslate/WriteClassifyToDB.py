from __future__ import print_function
import pymysql
def WriteClassifyToDB(name,classify):
    data = name
    department = classify
    connection = pymysql.connect(host='104.199.79.238', port=3306, user='root', passwd='123456', db='test')
    cun = connection.cursor()
    # Create a new record
    sql = "INSERT INTO `classifies` (`name`,`classify`) VALUES (%s,%s)"
    cun.execute(sql, (data,department))
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
    connection.close()