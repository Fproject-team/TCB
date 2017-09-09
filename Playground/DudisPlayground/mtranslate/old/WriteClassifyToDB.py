from __future__ import print_function
import pymysql
def WriteClassifyToDB(name,classify,vector,count):
    comp_name = name
    model = classify
    tfidf = vector
    count_v = count
    connection = pymysql.connect(host='104.199.79.238', port=3306, user='root', passwd='123456', db='test')
    connection.ping(True)
    cun = connection.cursor()
    # Create a new record
    sql = "INSERT INTO `classifies` (`comp_name`,`classify`,`vector`,`count`) VALUES (%s,%s,%s,%s)"
    cun.execute(sql, (comp_name, model, tfidf, count_v))
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
    connection.close()