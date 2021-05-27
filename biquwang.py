
from datetime import datetime
import openpyxl
from bs4 import BeautifulSoup
from lxml import *
from urllib import request
import time
"""
笔趣小说网（未登录）
"""
class BiXu(object):
    def __init__(self):
        self.start_url = 'https://www.duquanben.com/xiaoshuo/0/910/'
        self.headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

    def down_main(self):
        # 使用 openpyxl 进行下载下载成表格格式 方便再次清晰数据
        pass

    def details_urls(self, xs_dict):
        self.headers["Host"] = 'www.duquanben.com'
        self.headers["User-Agent"] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
        new_xs_list = []
        for xs_titele, url_text in xs_dict.items():

            response = request.Request(url=self.start_url+url_text, headers=self.headers, method='GET')
            resp = request.urlopen(response)
            html = resp.read().decode(encoding='GBK')
            soup = BeautifulSoup(html, 'lxml')
            tags = soup.select('#htmlContent')
            content_strs = tags[0].stripped_strings
            for content_str in content_strs:
                new_content_str = str(content_str)
                print(new_content_str)
            time.sleep(5)
            new_xs_list.append({
                'xs_titele':"xs_titele",
                'url_text':"url_text",
                'new_content_str':"new_content_str",
            })
        print(new_xs_list)

    def main(self):
        response = request.Request(url=self.start_url, headers=self.headers, method='GET')
        resp = request.urlopen(response)
        html = resp.read().decode(encoding='GBK')
        soup = BeautifulSoup(html, 'lxml')
        tags = soup.select('.mulu_list a')
        xs_dict = dict()
        for tag in tags:
            xs_title = tag.string
            href = tag.get('href')
            xs_dict[xs_title] = href
        self.details_urls(xs_dict)





bixu = BiXu()
if __name__ == '__main__':

    bixu.main()