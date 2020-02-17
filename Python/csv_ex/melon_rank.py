import requests
from bs4 import BeautifulSoup
import csv

url='https://www.melon.com/chart/index.htm'

user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
headers={
    'User-Agent':user_agent

}
res=requests.get(url,headers=headers).text
html=BeautifulSoup(res,'html.parser')

ranking=html.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis > span > a')

gasu2=html.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a:nth-child(2)')
gasu1=html.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a:nth-child(1)')

cnt=1
rank_list=[]
temp=[]

for ind,val in enumerate(ranking,1):
    tt=str(val)
    if 'goArtistDetail' in tt:
        temp.append(val.text)
    else:

        if temp:
            rank_dict['가수']=temp
            rank_list.append(rank_dict)
        rank_dict={
            'rank':f'{cnt}위',
            '곡명':val.text
        }
        cnt+=1
        temp=[]
    if ind==len(ranking):
        rank_dict['가수']=temp
        rank_list.append(rank_dict)

with open('melon_ranking.csv','w',encoding='utf-8',newline='') as csvfile:
    fieldnames=['rank','곡명','가수']
    csv_writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    csv_writer.writeheader()
    for rank in rank_list:
        csv_writer.writerow(rank)


