import datetime
import time

import pymysql
import re
import biliTop
import wangyimusic
import zhihu


def main():
    # bili链接
    biliurl = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
    wymusic_url = 'https://music.163.com/discover/toplist?id=3778678'
    qqmusic_url = 'https://u.y.qq.com/cgi-bin/musics.fcg?_=1660791650658&sign=zzb7abc3e3fhpp2ebhpx5gjxrmeuizf8w1aeb2454'
    zhihu_url = 'https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=100&desktop=true'
    # 数据库
    database = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'passwd': 'Doraemon903@CN',
        'db': 'hot_top',
        'charset': 'utf8'
    }

    # 逻辑判断
    b = datetime.date.today()
    bo = re.compile('....-..-(..)')

    # 网易音乐
    wangyimusic.wangyimusic(wymusic_url, database)
    # bilibili
    biliTop.bili(biliurl, database)
    # 知乎
    zhihu.zhihu(zhihu_url,database)



    # while (True):
    #     # 每天爬取
    #     biliTop.bili(biliurl, database)
    #
    #     # 两天一爬取
    #     if b:
    #         wangyimusic.wangyimusic(wymusic_url, database)
    #
    #     b = bool(1 - b)
    #     time.sleep(86400)


if __name__ == '__main__':
    main()
    print("已完成")
