import json

import pymysql

import askurl
import jsonpath


def zhihu(url, database):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15',
        'Referer': 'https://www.zhihu.com/hot'
    }
    request = askurl.getURL(url, header).encode('utf-8').decode('unicode-escape')
    # print(request)
    datalist = getdata(request)
    savedata(datalist, database)


def getdata(request):
    datalist = []
    jsonobj = json.loads(request)
    title = jsonpath.jsonpath(jsonobj, '$..title')
    id = jsonpath.jsonpath(jsonobj, '$..target.id')
    created = jsonpath.jsonpath(jsonobj, '$..created')
    excerpt = jsonpath.jsonpath(jsonobj, '$..excerpt')

    for item in range(len(title)):
        data = []
        data.append(title[item])
        url = 'https://www.zhihu.com/question/' + str(id[item])
        data.append(url)
        data.append(created[item])
        data.append(excerpt[item])

        datalist.append(data)
    # print(datalist)
    return datalist


def savedata(datalist, database):
    conn = pymysql.connect(host=database['host'], port=database['port'], user=database['user'],
                           passwd=database['passwd'], db=database['db'], charset=database['charset'])
    cn = conn.cursor()

    for data in datalist[:50]:
        for index in range(len(data)):
            if index == 2:
                data[index] = str(data[index])
                continue

            data[index] = '"' + data[index] + '"'

        sql = '''
            insert into zhihutop (
           title,url,created,excerpt)
            values(%s)''' % ",".join(data)

        print(sql)
        cn.execute(sql)

    conn.commit()

    cn.close()
    conn.close()



if __name__ == '__main__':
    zhihu(url='https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true', database={
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'passwd': 'Doraemon903@CN',
        'db': 'hot_top',
        'charset': 'utf8'
    })
