from os import replace
import urllib.request as ur
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with ur.urlopen(src) as response:
    data=json.load(response)
alist=data["result"]["results"]
with open("data.csv","w",encoding="utf-8") as file:
    for location in alist:
        a=location["file"].replace('jpghttps','jpg,https').replace('JPGhttps','JPG,https')
        b=a.split(",")
        c=b[0]
        file.write(location["stitle"]+","+location["address"][5:8]+","+location["longitude"]+","+location["latitude"]+","+c+"\n")
        
        
