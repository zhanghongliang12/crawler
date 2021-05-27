import requests
import time
import re
from lxml import etree
import openpyxl
"""
豆瓣租房小组-发布的豆瓣租房信息
必须设置睡眠时间-ip容易被豆瓣封一段时间

详情页也可以拿到 这里没有去取
"""
class doubanzufang(object):
    def __init__(self):
        self.start_url = 'https://www.douban.com/group/search'
        self.start_headers = {
            'Host': 'www.douban.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Cookie': 'bid=SyYLO8sTXHc; gr_user_id=7d27bda7-015b-4cce-8063-47df94a91e12; ct=y; ll="108288"; __yadk_uid=YHw4mVIdp3sG5PAjtpUgn0Fk3mZUOoHy; douban-fav-remind=1; __utmv=30149280.18648; viewed="2154713_26928415"; push_noty_num=0; __utmc=30149280; push_doumail_num=0; __gads=ID=37c295241a1c274e-227eb5d7dcc70090:T=1620366852:RT=1620366852:S=ALNI_MaZTBlfjon6JzMQLK3arX3KX25gHA; ap_v=0,6.0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1620379532%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DTYbIXFYoYpocOHZWpOna8w-PDjNw32Y54wlIIrf9tHd1oYS5uLSogG20NC6OgWb7%26wd%3D%26eqid%3De8571ba7000a3ee90000000260950785%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1940736702.1618993480.1620372206.1620379533.17; __utmz=30149280.1620379533.17.14.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_id.100001.8cb4=2746c2752e4a4975.1619079335.14.1620381044.1620368712.; __utmb=30149280.242.9.1620381044048',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
            'Referer': 'https://www.douban.com/group/search?start=0&cat=1019&sort=time&q=%E5%8C%97%E4%BA%AC%E7%A7%9F%E6%88%BF'
        }
        self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
            }
    def group_url_main(self, group_new_urls):
        wb = openpyxl.Workbook()
        sheet = wb.create_sheet()
        title_details_urls = []

        for group_new_url in group_new_urls:
            try:
                for i in range(0, 10):
                    i = i * 25
                    time.sleep(3)
                    new_url = group_new_url + f'discussion?start={i}'
                    print(new_url)
                    group_response = requests.get(url=new_url, headers=self.headers)
                    if group_response.status_code != 200:
                        break
                    group_html = group_response.content.decode('utf-8')
                    group_html_tree = etree.HTML(group_html)
                    group_infos = group_html_tree.xpath("//table[@class='olt']//tr[@class='']")
                    for group_info in group_infos:
                        details_url = group_info.xpath('./td[@class="title"]/a/@href')[0]  # 连接
                        title_text = group_info.xpath('./td[@class="title"]/a/text()')  # 连接
                        title_details_urls.append(details_url)
                        print(str(title_text[0]).strip())
                        sheet.append([
                            str(title_text[0]).strip(),
                            details_url
                        ])
            except Exception as e:
                continue



        wb.save('租房.xlsx')
    def start_main(self):
        i = 0
        group_new_urls = []
        while True:
            params = {
                'start': i,
                'cat': '1019',
                'sort': 'time',
                'q': '北京租房'
            }
            print(self.start_url)
            reaponse = requests.get(url=self.start_url, params=params, headers=self.start_headers)
            if reaponse.status_code == 200:
                html = reaponse.content.decode('utf-8')
                html_tree = etree.HTML(html)
                infos = html_tree.xpath('//div[@class="result"]')
                for info in infos:
                    group_new_url = info.xpath("./div[@class='pic']/a/@href")[0]
                    group_new_urls.append(group_new_url)

            else:
                break
            i += 20
        print(group_new_urls)
        self.group_url_main(group_new_urls=group_new_urls)


doubanzufang = doubanzufang()
if __name__ == '__main__':
    doubanzufang.start_main()


