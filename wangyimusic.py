import askurl
from bs4 import BeautifulSoup
import re
import pymysql


def wangyimusic(url, database):

    header = {
        'referer': 'https://music.163.com/discover/toplist?id=3778678',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    request = askurl.getURL(url, header)

    # print(request)
    datalist = getdata(request)
    savedata(datalist, database)


def getdata(request):
    datalist = []

    # soup = BeautifulSoup(request, "html.parser")

    # soup_find = soup.find_all('ul',class_="f-hide")
    # print(soup_find)
    findmusic = re.compile(r'<li><a href="/song\?id=(\d+)">(.*?)</a>')
    data = re.findall(findmusic, request)
    for i in data:
        datalist.append(list(i))
    # print(datalist)

    return datalist


def savedata(datalist, database):
    conn = pymysql.connect(host=database['host'], port=database['port'], user=database['user'],
                           passwd=database['passwd'], db=database['db'], charset=database['charset'])
    cn = conn.cursor()

    for item in datalist:
        for i in range(len(item)):
            if i == 0:
                item[i] = 'https://music.163.com/song?id=' + str(item[i])
            item[i] = '"' + item[i] + '"'
    # print(datalist)
        sql = '''
        insert into wymusic_top (
            wymusic_link,wymusic_title)
            values(%s)''' % ",".join(item)

        # print(sql)
        cn.execute(sql)
    conn.commit()

    cn.close()
    conn.close()



if __name__ == '__main__':
    print(' [1231]')
