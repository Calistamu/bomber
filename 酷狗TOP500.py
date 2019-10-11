import requests
from bs4 import BeautifulSoup
import time
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}
def get_info(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,"lxml")
    ranks = soup.select("span.pc_temp_num")
    titles = soup.select("div.pc_temp_songlist > ul > li > a")
    times = soup.select("span.pc_temp_tips_r")
    for rank,title,time in zip(ranks,titles,times):
       data = {
            "rank":rank.text.strip(),
            "singer":title.text.split("-")[0],
            "song":title.text.split("-")[1],
            "time":time.text.strip()
            }
       print(data)
if __name__=="__main__":
    urls=["http://www.kugou.com/yy/rank/home/{}-8888.html".format(i)for i in range(1,24)]
    for url in urls:
        get_info(url)
    time.sleep(2)
