from datetime import datetime
import urllib.request
from urllib import parse
import gzip
"""
中国天气网
"""
def main():
    city = input("输入城市")
    city_name = parse.quote(city)
    url = "http://toy1.weather.com.cn/search?cityname="+ city_name +"&callback=success_jsonpCallback&_=1621932728252"
    print(url)
    headers = dict()
    headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
    headers["Host"] = "toy1.weather.com.cn"
    headers["Accept-Encoding"] = "gzip"
    headers["Referer"] = "http://www.weather.com.cn/"
    headers["Cookie"] = "UM_distinctid=179a2a4a5be1db-0ec544d4422002-18281a0c-232800-179a2a4a5bfb6b; f_city=%E5%8C%97%E4%BA%AC%7C101010100%7C; csrfToken=K_jbOUFhQMLSzJY-SUhL-kMo; BAIDU_SSP_lcr=https://www.baidu.com/link?url=xTEO1imQJ2Lfk5dPbwpUS9i4fCFy6eFgAs8T3RLnXe8DWWt_NwGeS6vzz0gyhAUA&wd=&eqid=edcbbd68000c26a00000000260acbab6; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1621931370,1621932728; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1621932728"
    response = urllib.request.Request(url=url, method='GET', headers=headers)
    data = urllib.request.urlopen(response).read().decode('utf-8') # 读取信息
    print(data)
    html = gzip.decompress(data) # gzip

    print(html)


if __name__ == '__main__':
    main()









