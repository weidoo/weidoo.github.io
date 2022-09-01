import requests


def getURL(url, header):
    request = requests.get(url, headers=header)
    return request.text

def postURL(url:str, header:dict, data:dict):
    request = requests.post(url,header,data)
    return  request.text