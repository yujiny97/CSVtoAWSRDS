import csv
import io

def opencsv(filename):
    f=io.open(filename,'r' ,encoding='utf-8')
    rdr=csv.reader(f)
    a=[]
    for line in rdr:
        a.append(line)
    f.close()
    return a

def opencsv2(filename):
    f=io.open(filename,'rt' ,encoding='utf8')
    rdr=csv.reader(f)
    a=[]
    for line in rdr:
        a.append(line)
       # print(line)
    f.close()
    return a

#if __name__== "__main__":
#    opencsv2("/home/ec2-user/pythoncode/githubdata/coronaboard_kr/kr_regional_daily.csv")

