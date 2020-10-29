import csv
import io

#사실 utf-8이랑 utf8이랑 둘다 같다. 참고로 여기서 io.open 안하면 encoding이 제대로 안됨ㅠㅠ
#I think utf-8 and utf8 are just same.. and if I don't put "io" infront of open function, it cause error.
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

