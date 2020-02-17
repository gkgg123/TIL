import requests
import csv
from bs4 import BeautifulSoup


url='https://www.daum.net'
res=requests.get(url).text
html=BeautifulSoup(res,'html.parser')
# data=html.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li > div > div:nth-child(1) > span.txt_issue > a')
# rank={

# }
# cnt=1
# for d in data:
#     temp=str(cnt)+'위'
#     rank[temp]=d.text
#     cnt+=1
#     # print(d.text) ### tag들을 날리고 텍스트 파일을 구했다.


# print(rank)
# with open('rank.csv','w',encoding='utf-8',newline='') as rankfile:
#     csv_writer=csv.writer(rankfile)
#     for ind,val in rank.items():
        # csv_writer.writerow([ind,val])


#### 강사님 방법 #####
rankings=html.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li > div > div:nth-child(1) > span.txt_issue > a')
rank_list=[]
for ind,rank in enumerate(rankings,1):
    # rank_dict[f'{ind}위']=rank.text
    rank_dict={
        'rank': f'{ind}위',
        'value':rank.text
    }
    rank_list.append(rank_dict)
print(rank_list)

with open('ranking.csv','w',encoding='utf-8',newline='') as csvfile:
    # csv_writer=csv.writer(csvfile)
    fieldnames=['rank','value']
    csv_writer=csv.DictWriter(csvfile,fieldnames=fieldnames) ### DictWriter로 교체
    csv_writer.writeheader()
    for rank in rank_list:        
        csv_writer.writerow(rank)


