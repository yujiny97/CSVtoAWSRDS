import sys
import os
import base64
import json
import logging
import time
import pymysql
import opencsv as oc


host = "database-1.#######.ap-northeast-1.rds.amazonaws.com" # my RDS end point
port = 3306
usern="" #my username
pw="" # my password
database="" #my database name

def main():
    conn,cursor=connect_RDS(host,port,usern,pw,database)
    data=[]
    data2=[]
    data=oc.opencsv("./githubdata/coronaboard_kr/kr_daily.csv");
    data2=oc.opencsv2("./githubdata/coronaboard_kr/kr_regional_daily.csv");
    for i in range(1,len(data)):
        qry=insert_function(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5])
        cursor.execute(qry)
    for i in range(1,len(data2)):
        qry=insert_function2(data2[i][0],data2[i][1],data2[i][2],data2[i][3],data2[i][4])
        #if(i==1):
        #print(qry)
        cursor.execute(qry)
    conn.commit()

def insert_function(dt,cf,de,re,te,ne): #insert query
    return "insert ignore into Daily(date,confirmed,death,released,tested,negative) values('"+str(dt)+"',"+str(cf)+","+str(de)+","+str(re)+","+str(te)+","+str(ne)+");"

def insert_function2(dt,reg,cof,de,re): #insert query
    return "insert ignore into Regional_Daily(Date_re,region,confirmed,death,released) values('"+str(dt)+"','"+str(reg)+"',"+str(cof)+","+str(de)+","+str(re)+");"

def connect_RDS(host,port,usern,pw,database):
    try:
        conn=pymysql.connect(host,user=usern,passwd=pw,db=database,connect_timeout=5,
        port=port,use_unicode=True,charset='utf8')
        cursor=conn.cursor()
    except Exception as ex:
        logging.error("RDS failed.")
        print(ex)
        sys.exit(1)
    return conn,cursor

if __name__=="__main__":
    main()
