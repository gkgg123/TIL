import csv
lunch={
    '그릴스':'매운돈까스',
    '소반':'낙곱새'
}

# csvfile=open('lunch.csv','w',encoding='utf-8',newline='')
# ### 데이터 입력과정 ###
# ### csvfile 3번째 위치에 encoding='utf-8' 을 추가하면 한글이 안꺠진다.
# ### newline='' 을 하면 이어서 나온다!!!!!
# csv_writer=csv.writer(csvfile)
# for ind,val in lunch.items():
#     csv_writer.writerow([ind,val])

# # csv_writer.writerow(['그릴스','매운돈까스'])
# # csv_writer.writerow(['소반','낙곱새'])
# csvfile.close()
# #### 데이터를 닫는행위 ###



with open('lunch.csv','w',encoding='utf-8',newline='') as csvfile:
    csv_writer=csv.writer(csvfile)
    for ind,val in lunch.items():
        csv_writer.writerow([ind,val])
