import datetime
import re
import time
import pymysql
import askurl
import execjs


def getdata(database):
    conn = conn = pymysql.connect(host=database['host'], port=database['port'], user=database['user'],
                                  passwd=database['passwd'], db=database['db'], charset=database['charset'])
    cn = conn.cursor()
    select = '''
    select * from bilitop_copy1
    '''
    cn.execute(select)
    data = cn.fetchall()
    # print(data)
    cn.close()
    conn.close()

    datadic = {}
    for item in data:
        datadic.update({item[1]: item[3]})
    # print(datadic)
    return data


if __name__ == '__main__':
    database = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'passwd': 'Doraemon903@CN',
        'db': 'hot_top',
        'charset': 'utf8'
    }

    getdata(database)
