import askurl


def qqmusic(url):
    header = {
        'referer': 'https://y.qq.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    data = {"comm": {"cv": 4747474, "ct": 24, "format": "json", "inCharset": "utf-8", "outCharset": "utf-8", "notice": 0,
                  "platform": "yqq.json", "needNewCode": 1, "uin": 0, "g_tk_new_20200303": 5381, "g_tk": 5381},
         "req_1": {"module": "musicToplist.ToplistInfoServer", "method": "GetDetail",
                   "param": {"topid": 26, "offset": 0, "num": 20, "period": "2022-08-17"}}}

    request = askurl.postURL(url,header,data)
    print(request)



if __name__ == '__main__':
    qqmusic_url = 'https://u.y.qq.com/cgi-bin/musics.fcg?_=1660791650658&sign=zzb7abc3e3fhpp2ebhpx5gjxrmeuizf8w1aeb2454'
    qqmusic(qqmusic_url)