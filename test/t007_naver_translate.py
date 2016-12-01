# -*- coding: utf-8 -*-
import os
import sys
import urllib.request
import json

def t007():
    client_id = "Qy52IxKG9mpkq8TTmo7H"
    client_secret = "VOzPjguhTL"
    encText = urllib.parse.quote("나는 누구인가요?")
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/language/translate"
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(req, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        data = response.read()
        data = data.decode('utf-8')
        js = json.loads(data)
        print("[TEST007]")
        print('\t', js['message']['result']['translatedText'])
        return 0
    else:
        return -1