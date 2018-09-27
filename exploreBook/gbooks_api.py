import os
import requests
import csv
import json

class gbooks():
    googleapikey="AIzaSyARiG1OaylTsDSpSEYjqp-dgBkZfUamd9o"

    def search(self, value):
        params = {"q":value, 'key':self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=params)
        #print (r.url)
        rj = r.json()
        #print (rj["totalItems"])
        for i in rj["items"]:
            try:
                title = repr(i["volumeInfo"]["title"])
                url = (repr(i["volumeInfo"]["previewLink"]))
                return title,url
            except:
                pass
            try:
                
                return url
            except:
                pass
            #try:
                #print (repr(i["volumeInfo"]["imageLinks"]["thumbnail"]))
            #except:
                #pass

if __name__ == "__main__":
    bk = gbooks()
    #bk.search("stephen king")

with open('csvFold.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    i = next(reader)  # Skip the header row.
    for row in reader:
        print(bk.search(row[1]))


