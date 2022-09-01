import pymysql


def getHotspotData():
    database = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'passwd': 'Doraemon903@CN',
        'db': 'hot_top',
        'charset': 'utf8'
    }
    conn = pymysql.connect(host=database['host'], port=database['port'], user=database['user'],
                               passwd=database['passwd'], db=database['db'], charset=database['charset'])
    cn = conn.cursor()

    bilisql = '''
    select * from bilitop where TO_DAYS(hotdate) = TO_DAYS(NOW())
    '''
    wymusicsql = '''
    SELECT * FROM wymusic_top WHERE TO_DAYS(wymusic_date) = TO_DAYS(NOW())
    '''
    cn.execute(bilisql)
    bilidata = cn.fetchall()
    print(bilidata)

if __name__ == '__main__':
    getHotspotData()