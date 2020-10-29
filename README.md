# CSV file to AWS RDS
csv file reference: https://github.com/jooeungen/coronaboard_kr  

RDS에 자동으로 github에 있는 CSV 파일을 다운받아서 import 해주는 코드입니다. (이 csv 파일은 매일 업데이트 됩니다.)  
public에 있는 EC2 인스턴스에서 private subnet에 있는 RDS로 접속하도록 하면 됩니다.  

This code automatically downloads and imports the CSV file from github to RDS. (This csv file is updated daily.)  
This can be done by having an EC2 instance in public subnet connect to the RDS in a private subnet.  

# 파일 정보 (file information)
imptords.py : rds와 연결해서 csv파일에서 값들을 가져와 import 해주는 python 코드  
csv -> rds  

opencsv.py : gihub로부터 clone 시킨 csv파일들을 2차원 list로 변경해주는 코드  
read csv  

autodata.sh : github에서 clone하는것부터 파이썬 코드를 실행시켜 rds에 값을 넣어주는 과정까지 진행    
clone github -> execute imptords.py  

crontab.txt : crontab -e 설정  


imptords.py: python code that connects to rds and imports values from csv file
csv -> rds

opencsv.py: Code that converts csv files cloned from gihub into a two-dimensional list
read csv

autodata.sh: From github to clone to execute Python code and put values into rds
clone github -> execute imptords.py

crontab.txt: crontab -e setting

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

