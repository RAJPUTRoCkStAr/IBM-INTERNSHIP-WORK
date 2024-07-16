from bs4 import BeautifulSoup
import pandas as pd
import os 
d = {'title':[],'price':[]}
for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc,'html.parser')
        t = soup.find("div",class_="KzDlHZ")
        title = t.get_text()
        p = soup.find("div",class_="Nx9bqj _4b5DiR")
        price = p.get_text().strip('â‚¹')
        d['title'].append(title)
        d['price'].append(price)
    except Exception as e:
        print(e)
df = pd.DataFrame(data=d)
df.to_csv("data/data.csv")