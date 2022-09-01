import json
import jsonpath
import pymysql
import askurl


def bili(biliurl, database):
    headers = {
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    request = askurl.getURL(biliurl, headers)
    # print(request)
    datalist = getDate(request)
    savedata(datalist, database)


# 获取数据
def getDate(request):
    # date = re.findall(r'"list":(.*?)}}', request)

    datalist = []

    jsonobj = json.loads(request)
    # 视频标题
    title = jsonpath.jsonpath(jsonobj, '$..title')
    # 视频图片
    pic = jsonpath.jsonpath(jsonobj, '$..pic')
    # 播放链接
    short_link = jsonpath.jsonpath(jsonobj, '$..short_link')
    # 播放数
    view = jsonpath.jsonpath(jsonobj, '$..view')
    # up主
    name = jsonpath.jsonpath(jsonobj, '$..name')

    for i in range(len(title)):

        savedate = []
        # 保存:视频标题 图片 链接 播放数 up主
        savedate.append(title[i])
        savedate.append(pic[i])
        savedate.append(short_link[i])
        savedate.append(view[i])
        savedate.append(name[i])

        datalist.append(savedate)

    # print(datalist)
    return datalist


# 保存数据
def savedata(datalist, database):
    conn = pymysql.connect(host=database['host'], port=database['port'], user=database['user'],
                           passwd=database['passwd'], db=database['db'], charset=database['charset'])
    cn = conn.cursor()

    for data in datalist[:100]:
        for index in range(len(data)):
            if index == 3:
                data[index] = str(data[index])
                continue

            data[index] = '"' + data[index] + '"'


        sql = '''
        insert into bilitop (
            title,pic_link,short_link,view_num,uper)
            values(%s)''' % ",".join(data)

        print(sql)
        cn.execute(sql)

    conn.commit()

    cn.close()
    conn.close()

if __name__ == '__main__':
    biliurl = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
    bili(biliurl)
