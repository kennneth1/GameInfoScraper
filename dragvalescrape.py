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
print("testing", len(inv)*len(inv), "possible combinations")

total = len(inv)*len(inv)

c = 0
entire = []
for dragon in inv:
    drag1=home_page+"#d1="+dragon
    for drag in inv:
        full_page = drag1+";d2="+drag
        print(full_page)
        browser = webdriver.Chrome("C:/Users/huangk/Desktop/chromedriver.exe")
        browser.get(full_page)
        time.sleep(1)
        html = browser.page_source
        soup = BeautifulSoup(html, features='html.parser')
        data = [element.text for element in soup.findAll('div', attrs={'class':'center','id': 'by_type'})]
        try:
            data = data[0] # convert to string
            ind = data.find('Epic')
            print(data)
            if ind != -1:
                entire.append([dragon,drag,data[ind:ind+10]])
        except IndexError:
            pass
        browser.close()
        c+=1
        print("Program is", (c/total)*100, "% complete")
        
        print("Est time till complete:"

df = pd.DataFrame(entire, columns = ['dragon 1', 'dragon 2', 'total % for epic'])
df['total % for epic'] = df['total % for epic'].str[7:].astype(int)
df.sort_values(by=['col1'], ascending=False)
print(df)
df.to_csv(r'C:\Users\huangk\Desktop\best_epics.csv', index = False, header=True)


