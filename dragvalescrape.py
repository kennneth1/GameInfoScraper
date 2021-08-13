import selenium
from bs4 import BeautifulSoup
import csv 
import time
from selenium import webdriver
import requests
import pandas as pd

f = open('drag.txt')
inv = []
for row in csv.reader(f):
    inv.append(row)
inv = inv[0]

print("input data is of length: ", len(inv))


c=0
# list = [a,b,c,d]
# 3+2+1 = 6
# [a,b,c,d,e]
# 4+3+2+1 = 10
# (len(list)-1)
entire = []
for i in range(0, len(inv)-1):
    for j in range(i+1, len(inv)):
        link = 'https://dvbox.bin.sh/#d1=' + inv[i] + ";d2=" + inv[j]
        print(link)
        browser = webdriver.Chrome("C:/Users/huangk/Desktop/chromedriver.exe")
        browser.get(link)
        time.sleep(0.5)
        html = browser.page_source
        soup = BeautifulSoup(html, features = "html.parser")
        data = [element.text for element in soup.findAll('div', attrs={'class':'center','id': 'by_type'})]
        try:
            data = data[0] # convert to string
            ind = data.find('Epic')
            print(data)
            if ind != -1:
                entire.append([inv[i],inv[j],data[i:ind+10]])
        except IndexError:
            pass
        except TimeoutException:
            pass
        browser.close()
        c+=1
        print("Program is", round(c/1596,3)*100, "% complete")

              
df = pd.DataFrame(entire, columns = ['dragon 1', 'dragon 2', 'epic'])
df['epic'] = df['epic'].str[7:]
df.sort_values(by=['epic'], ascending=False)
print(df)
df.to_csv(r'C:\Users\huangk\Desktop\dragon_output_final.csv', index = False, header=True)


