# CSV file to AWS RDS
csv file reference: https://github.com/jooeungen/coronaboard_kr  

RDS에 자동으로 github에 있는 CSV 파일을 다운받아서 import 해주는 코드입니다.  

# 파일 정보 (file information)
imptords.py : rds와 연결해서 csv파일에서 값들을 가져와 import 해주는 python 코드
csv -> rds  

opencsv.py : gihub로부터 clone 시킨 csv파일들을 2차원 list로 변경해주는 코드
read csv  

autodata.sh : github에서 clone하는것부터 파이썬 코드를 실행시켜 rds에 값을 넣어주는 과정까지 진행  
clone github -> execute imptords.py  

crontab.txt : crontab -e 설정  

# table 정보 (table information)

Daily  
date(PK) date  
confirmed int  
death int  
released int  
tested int  
negative int  

Regional_Daily  
Date_re(PK) date  
region(PK) varchar(45)  
confirmed int  
death int  
released int  
