import pymysql

from DudisPlayground.mtranslate.Classify.DB import ReadFromDBDBOrganize as train


class TrainData:
    id = []
    data = []
    target = []

traindata = train.ReadFromDB('Harel')
num = 0
for i in range(len(traindata.data)):
    try:
        #print i
        traindata.data[i].decode().encode('utf-8').strip()
    except Exception:
        connection = pymysql.connect(host='104.199.79.238', port=3306, user='root', passwd='123456', db='test')
        cun = connection.cursor()
        sql = "DELETE FROM `DBOrganize` WHERE id = '%s'"
        cun.execute(sql, (traindata.id[i],))
        connection.commit()
        connection.close()
