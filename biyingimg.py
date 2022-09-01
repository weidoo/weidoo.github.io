import askurl


def bingimg():
    html = "https://bing.ioliu.cn/"
    headers = {
        "Referer": html,
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive'
    }
    request = askurl.getURL(html,headers)
    print(request)

if __name__ == '__main__':
    bingimg()