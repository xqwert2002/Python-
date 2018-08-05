import urllib.request as request
import json #使用json資料格式 (JavaScript Object Notation)
with request.urlopen("http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=36847f3f-deff-4183-a5bb-800737591de5") as response:
    data=json.load(response)

keyword=input("搜尋捷運站:")
file=open("Taipei.txt","w",encoding="utf-8")

list=data["result"]["results"]

for MRT in list:
    if keyword in MRT["MRT"]:
        sites=MRT["stitle"]
        file.write(sites)
        file.write("\n")

file.close()