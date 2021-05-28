
from datetime import datetime
import requests
import json
import time
"""
酷我音乐下载
GET 请求
"""
class KuWoMusic():
    def __init__(self):
        self.url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={name}&pn={page}&rn=30&httpsStatus=1&reqId=571c1971-bf6a-11eb-8c32-0155a82d330d"
        self.headers = {
            "Accept":"application/json, text/plain, */*",
            "Accept-Encoding":"gzip, deflate",
            "Connection":"keep-alive",
            "Cookie":"Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1622174890; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1622174890; _ga=GA1.2.661384117.1622174890; _gid=GA1.2.1304559704.1622174890; _gat=1; kw_token=KVM7FW7F84S",
            "csrf":"KVM7FW7F84S",
            "Host":"www.kuwo.cn",
            "Referer":"http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
        }

    def download(self, music_name, music_url):
        """下载音乐"""
        response = requests.get(music_url)
        content = response.content
        self.save_file(music_name + '.mp3', content)

    def save_file(self, filename, content):
        """保存音乐"""
        with open(file='音乐/'+filename, mode="wb") as f:

            f.write(content)

    def download_music(self, music_lists):
        for info in music_lists:
            url = f"http://www.kuwo.cn/url?format=mp3&rid={info['rid']}&response=url&type=convert_url3&br=128kmp3&from=web&t=1622192638040&httpsStatus=1&reqId=a2fb5491-bf93-11eb-8c32-0155a82d330d"
            response = requests.get(url=url, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                download = self.download(info["name_ch"], music_url=data["url"])
                print(f'-------------------------{info["name_ch"]}--下载完毕')
                time.sleep(0.5)
            time.sleep(1)

    def main(self):
        name = str(input("请输入歌手名："))
        max_page = int(input("请输入下载的页数："))
        for page in range(1, max_page+1):
            request_url = self.url.format(name=name, page=page)
            response = requests.get(url=request_url, headers=self.headers)
            music_lists = []
            if response.status_code == 200 and response.json():
                json_data = response.json()
                if json_data["code"] == 200:
                    data_lists = json_data["data"]["list"]  # 音乐列表
                    total = json_data["data"]["total"]
                    for music_details_data in data_lists:
                        name_ch = music_details_data["album"]  # 名称
                        rid = music_details_data["rid"]  #
                        music_lists.append({
                            "name_ch": name_ch,
                            "rid": rid,

                        })
            self.download_music(music_lists=music_lists)
            time.sleep(3)

kuwo_music = KuWoMusic()
kuwo_music.main()
