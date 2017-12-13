# _*_ coding:utf-8 _*_


import urllib
import requests


def url_quote():
    raw_url = 'http://bs2-audiorec.oss-cn-shanghai.aliyuncs.com/e98f81fb526061e92a26eda17955c219.pcm'
    url = urllib.quote(raw_url)
    print url
    # http%3A//bs2-audiorec.oss-cn-shanghai.aliyuncs.com/e98f81fb526061e92a26eda17955c219.pcm
    print urllib.unquote(url)
    # http://bs2-audiorec.oss-cn-shanghai.aliyuncs.com/e98f81fb526061e92a26eda17955c219.pcm
    print urllib.quote("河=&源")
    # %E6%B2%B3%E6%BA%90


def req_with_para():
    d_para = {"name": "xy", "age": 21}
    print requests.get('http://xy.com', params=d_para)

    # ordered name-value pairs
    d_sorted_para = [("age", 21), ("name", "xy")]
    print requests.get('http://xy.com', params=d_sorted_para)


def url_encode_v1():
    f = {'eventName': 'myEvent', 'eventDescription': '飞龙在天'}
    print urllib.urlencode(f)
    # eventName=myEvent&eventDescription=%E9%A3%9E%E9%BE%99%E5%9C%A8%E5%A4%A9


def url_encode_v2():
    d_para = {"name": "xy熊大", "age": 21}
    print '&'.join('%s=%s' % (k, v) for k, v in d_para.iteritems())
    # age=21&name=xy熊大
    print '&'.join('%s=%s' % (k, urllib.quote(str(v))) for k, v in d_para.iteritems())
    # age=21&name=xy%E7%86%8A%E5%A4%A7

    base_url = 'xy.com/'
    url = 'http://%s?%s' % (base_url, '&'.join('%s=%s' % (k, urllib.quote(str(v))) for k, v in d_para.iteritems()))
    print url
    # http://xy.com/?age=21&name=xy%E7%86%8A%E5%A4%A7

    print urllib.unquote(url)
    # http://xy.com/?age=21&name=xy熊大


def post_request_tw():
    d_para = {"mp4Url": "https://bilinimg.bs2ul-ssl.yy.com/android2222.mp4",
              "secretKey": "XY-bl-audio-rec-text-ret",
              "serial": "17598411"}

    print urllib.urlencode(d_para)

    # rsp = requests.get('http://172.27.49.16:8887/bilin/audiorec/', params=d_para)
    rsp = requests.get('http://61.147.186.82:9997/bilin/audiorec/', params=d_para)
    print rsp.content

    s = "sign=75dd4677e941482f882b59bd2aee7fc1&text=%E4%B8%80%E4%BA%8C%E4%B8%89%E5%9B%9B%E4%BA%94%E5%85%AD%E4%B8%83%E5%85%AB%E4%B9%9D%E5%8D%81%E4%B8%80%E4%BA%8C%E4%B8%89%E5%9B%9B%E4%BA%94%E5%85%AD%E4%B8%83%E5%85%AB%E4%B9%9D%E5%8D%81%EF%BC%8C&ts=1513157485&code=0&serial=175984"
    print urllib.unquote(s)

if __name__ == '__main__':
    post_request_tw()
    # url_quote()
    # url_encode_v1()
    # url_encode_v2()
    pass
